#! /usr/bin python3
#conding: utf-8

import requests
import json
import sys
import mysql.connector
from passlib.hash import pbkdf2_sha256
from getpass import getpass

# My module
import constants as const

#-------------Classes---------------------------------------------------------
class DataBase():

    def __init__(self, name_BDD):
        self.name_BDD = name_BDD
        self.conn = None
        self.cursor = None
        self.colect_data = None

    def connexion(self, host, user, passwd):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            passwd = passwd,
            database = self.name_BDD
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, *args):
        req = "INSERT INTO {} ({}) VALUES ({});".format(*args)
        #import pdb; pdb.set_trace()
        self.__execute(req)
        self.__commit()

    def select_data(self, donnees, table, where, cond):
        if where == None and cond == None:
            req1 = "SELECT {} FROM {}".format(donnees, table)
            #import pdb; pdb.set_trace()
            self.__execute(req1)
            self.colect_data = self.cursor.fetchall()

        else:
            req = "SELECT {} FROM {} WHERE {} = '{}'"
            req = req.format(donnees, table, where, cond)
            #import pdb; pdb.set_trace()
            self.__execute(req)
            self.colect_data = self.cursor.fetchall()

    def close(self):
        self.conn.close()

    def __execute(self, *args):
        self.cursor.execute(*args)

    def __commit(self):
        self.conn.commit()


class User():

    def __init__(self, select):
        self.select = select
        self.passwd = None
        self.rep = None
        self.tent = 0

    def choice(self):
        self.rep = input(self.select)
        return self.rep

    def sign_in(self, db):
        print("\nVeuillez renseigner votre identifiant: ")
        self.choice()
        db.select_data("user_name", "pb_users", "user_name", self.rep)
        #import pdb; pdb.set_trace()
        if db.colect_data[0][0] == self.rep:
            print("Identifiant correct,")
            print("merci de renseignez votre mot de passe:")
            if self.__password(db, create=False):
                print("Mot de passe correct")
        else:
            print("\nL'identifiant n'existe pas, merci de recommencer !")
            self.sign_in(db)

    def sign_up(self, db):
        print("\nVeuillez renseigner un identifiant pour votre compte: ")
        self.choice()
        db.select_data("user_name", "pb_users", "user_name", self.rep)
        if db.colect_data == []:
            print("Identifiant libre,")
            print("merci de renseignez un mot de passe:")
            if self.__password(db, create=True):
                values = "'{}', '{}'".format(self.rep, self.passwd)
                db.insert_data("pb_users", "user_name, user_passwd", values)
                print("Identifiant créez avec succès :-)")


    def __password(self, db, create):
        if create:
            pwd = getpass()
            hashed = pbkdf2_sha256.hash(pwd)
            if pbkdf2_sha256.verify(pwd, hashed):
                self.passwd = hashed
                return True
            else:
                return False
        else:
            pwd = getpass()
            db.select_data("user_passwd", "pb_users", "user_name", self.rep)
            if pbkdf2_sha256.verify(pwd, db.colect_data[0][0]):
                return True
            else:
                self.tent += 1
                print("Mot de passe incorrect, tentative {}/3".format(self.tent))
                if self.tent == 3:
                    return False
                else:
                    self.__password(db)


#-----------------------------------------------------------------------------


#-------------Fonctions-------------------------------------------------------
def check(user, cond):
    if user.rep in cond:
        pass

    else:
        print("Mauvaise réponse")
        user.choice()
        check(user, cond)

def search(user, db):
    cond = []
    db.select_data("*", "pb_categories", where=None, cond=None)

    print("\nSélectionnez une catégorie :\n")
    for x in db.colect_data:
        print("{} - {}".format(x[0], x[1]))
        cond.append(str(x[0]))
    user.choice()
    check(user, cond)

    print("\nSélectionnez un aliment :\n")
    foo = int(user.rep)-1
    done = db.colect_data[foo][1]
    db.select_data("aliment_name", "pb_aliments", "aliment_categorie", done)
    nb = 0
    for x in db.colect_data:
        nb += 1
        print("{} - {}".format(nb, x[0]))
        cond.append(nb)
    user.choice()
    check(user, cond)
    data = "aliment_name, aliment_shop, aliment_link"
    where = "aliment_name"
    foo = int(user.rep)-1
    done = db.colect_data[foo][0]
    db.select_data(data, "pb_aliments", where, done)
    print("\nAliment sélectionnez : {}".format(db.colect_data[0][0]))
    print("\nBoutique : {}".format(db.colect_data[0][1]))
    print("\nLien internet : {}\n".format(db.colect_data[0][2]))

#-----------------------------------------------------------------------------




db = DataBase("purbeurre")
db.connexion(const.HOST, const.USER, const.PWD)
user = User(const.USERCHOICE)
def main():

    print("\n\n\tBonjour et bienvenu sur PurBeurreRecherche !!!\n")
    print("Choisissez une option: [1 ou 2]\n")
    print("1- {}\n2- {}".format(const.QUESTIONS[1], const.QUESTIONS[2]))
    user.choice()
    check(user, const.REP1)

    if user.rep == "1":

        search(user, db)
        print(const.QUESTIONS[5])
        user.choice()
        check(user, const.REP)
        if user.rep == "o" or user.rep == "O":
            print("Choisissez une option: [1 ou 2]\n")
            print("1 - Connexion\n2 - Création de compte")
            user.choice()
            check(user, const.REP1)
            if user.rep == "1":
                user.sign_in(db)

            elif user.rep == "2":
                user.sign_up(db)

    elif user.rep == "2":

        user.sign_in(db)
        print("Aliment chercher:  ")
        #Afficher les aliments cherchés
        print("Substitut enregistrés:  ")
        #Afficher les substituts enregistrés
        print("Choisissez une option: [1 ou 2]\n")
        print("1- {}\n2- {}".format(const.QUESTIONS[6], const.QUESTIONS[7]))
        user.choice()
        check(user, const.REP1)

        if user.rep == "1":

            search(user)

        elif user.rep == "2":
            db.close()
            sys.exit()


main()
db.close()