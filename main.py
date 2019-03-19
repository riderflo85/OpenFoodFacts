#! /usr/bin python3
# conding: utf-8

import requests
import sys

# My module
from config import constants as const
from config import fonctions as fonc
from config.DataBase import DataBase
from config.User import User

db = DataBase("purbeurre")
db.connexion(const.HOST, const.USER, const.PWD)
user = User(const.USERCHOICE)

print("\n\n\tBonjour et bienvenu sur PurBeurreRecherche !!!\n")
print("Choisissez une option: [1 ou 2]\n")
print("1- {}\n2- {}".format(const.QUESTIONS[1], const.QUESTIONS[2]))
user.choice()
fonc.check(user, const.REP1)


def main():

    if user.rep == "1":
        fonc.search(user, db)
        fonc.substitute(db)

        print(const.QUESTIONS[5])
        user.choice()
        fonc.check(user, const.REP)

        if user.rep == "o" or user.rep == "O":
            print("Choisissez une option: [1 ou 2]\n")
            print("1 - Connexion\n2 - Création de compte")
            user.choice()
            fonc.check(user, const.REP1)

            if user.rep == "1":
                user.sign_in(db)
                db.select_where("id_aliments", "pb_aliments", "aliment_name",
                    db.result)
                db.insert_data("pb_favoris", "favoris_aliment",
                    db.colect_data[0][0])
                print("\nEnregistrement réussi")

            elif user.rep == "2":
                user.sign_up(db)
                db.select_where("id_aliments", "pb_aliments", "aliment_name",
                    db.result)
                db.insert_data("pb_favoris", "favoris_aliment",
                    db.colect_data[0][0])
                print("\nEnregistrement réussi")

        if fonc.end(user):
            main()

        else:
            db.close()
            sys.exit()

    elif user.rep == "2":
        user.sign_in(db)
        print("\nAliment chercher:  ")
        # Afficher les aliments cherchés
        arg = ["pb_favoris", "id_aliments", "favoris_aliment"]
        db.select_join("aliment_name", "pb_aliments", *arg)
        print(db.colect_data[0][0])

        print("\nSubstitut enregistrés:  ")
        # Affiche les substituts enregistrés

        if fonc.end(user):
            main()

        else:
            db.close()
            sys.exit()


main()
db.close()
