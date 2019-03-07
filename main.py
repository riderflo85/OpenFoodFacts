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
        self.__commit()
    
    def select_data(self, donnees, table):
        req = "SELECT {} FROM {}".format(donnees, table)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()
        return self.colect_data
    
    def close(self):
        self.conn.close()

    def __execute(self, *args):
        self.cursor.execute(*args)
    
    def __commit(self):
        self.conn.commit()


class User():

    def __init__(self, select):
        self.select = select
        self.rep = None
    
    def choice(self):
        self.rep = input(self.select)
        return self.rep

#-----------------------------------------------------------------------------


#-------------Fonctions-------------------------------------------------------
def check(user, cond):
    if user.rep in cond:
        print("la réponse est dans la liste")

    else:
        print("Mauvaise réponse")
        user.choice()
        check(user, cond)

def encoding(db):
    tent = 0
    user_passwd = getpass()
    key = pbkdf2_sha256.hash(user_passwd)
    db.select_data(key, "users")
    done = pbkdf2_sha256.verify(db.colect_data, key)
    if done:
        return True
    else:
        tent += 1
        print("Mot de passe incorrect, tentative {}/3".format(tent))
        encoding(db)
        if tent == 3:
            return False

def search(user):
    cond = []
    print("\nSélectionnez une catégorie :\n")
    for k, v in const.CATEGORIES.items():
            print("{} - {}".format(k, v))
            cond.append(str(k)) 
    user.choice()
    check(user, cond)

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

        search(user)

    elif user.rep == "2":

        print("Veuillez renseigner votre identifiant: (même si vous en avez\
 pas encore)")
        user.choice()
        db.select_data(user.rep, "users")

        if user.rep == db.colect_data:

            print("Identifiant correct, merci de renseignez votre mot de\
 passe:")
            if encoding(db):

                print("Mot de passe correct")
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

            else:

                print("Vous avez fait trois tentatives sans succès, vos\
 favoris ne sont pas accessible. Le programme se relance...")
                main()



main()
db.close()