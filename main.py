#! /usr/bin python3
#conding: utf-8

import requests
import json
import mysql.connector
# My module
import constants

class DataBase():

    def __init__(self, name_BDD):
        self.name_BDD = name_BDD
        self.conn = None
        self.cursor = None
    
    def connexion(self, host, user, passwd):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            passwd = passwd,
            database = self.name_BDD
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, *args):
        pass
    
    def select_data(self, donnees, table):
        req = "SELECT {} FROM {}".format(donnees, table)
        _execute(req)
        self.colect_data = self.cursor.fetchall()
        return self.colect_data

    def _execute(self, *args):
        self.cursor.execute(*args)
    
    def _commit(self):
        self.conn.commit()


class User():

    def __init__(self, select):
        self.select = select
        self.rep = None
    
    def choice(self):
        self.rep = input(self.select)
        return self.rep

def check(user, cond):
    if user.rep in cond:
        print("la réponse est dans la liste")

    else:
        print("Mauvaise réponse")
        user.choice()
        check(user, cond)

def main():
    user = User(constants.USERCHOICE)
    cond = []

    print("\n\n\tBonjour et bienvenu sur PurBeurreRecherche !!!\n")
    print("Choisissez une option: [1 ou 2]\n")
    print("1- {}\n2- {}".format(constants.QUESTIONS[1], constants.QUESTIONS[2]))
    user.choice()
    check(user, constants.REP1)
    if user.rep == "1":
        print("\nSélectionnez une catégorie :\n")
        for k, v in constants.CATEGORIES.items():
            print("{} - {}".format(k, v))
            cond.append(str(k))
        user.choice()
        check(user, cond)
    

main()