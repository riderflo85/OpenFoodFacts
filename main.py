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
                fonc.save(db, user.user_id)

            elif user.rep == "2":
                user.sign_up(db)
                fonc.save(db, user.user_id)

        if fonc.end(user):
            main()

        else:
            db.close()
            sys.exit()

    elif user.rep == "2":
        user.sign_in(db)

        data = "aliment_name, aliment_link"
        where = "id_users"
        cond = user.user_id
        arg = ["pb_favoris", "id_aliments", "favoris_aliment"]
        db.select_where_join(data, "pb_aliments", where, cond, *arg)
        result_name = []
        result_link = []

        for x in db.colect_data:
            result_name.append(x[0])
            result_link.append(x[1])

        print("-------------------------------------------------------------")
        print("\n\t\tAliment chercher:")
        print("\tNom des aliments:\n")

        index = 0
        for x in result_name:
            index += 1
            print("{} - {}".format(index, x))

        print("\n\tLien internet pour plus d'infos:\n")

        index = 0
        for x in result_link:
            index += 1
            print("{} - {}".format(index, x))

        # Affiche les substituts enregistrés
        data = "aliment_name, aliment_link"
        where = "id_users"
        cond = user.user_id
        arg = ["pb_favoris", "id_aliments", "favoris_substitute"]
        db.select_where_join(data, "pb_aliments", where, cond, *arg)
        result_name = []
        result_link = []

        for x in db.colect_data:
            result_name.append(x[0])
            result_link.append(x[1])
        print("-------------------------------------------------------------")

        print("-------------------------------------------------------------")
        print("\n\t\tSubstitus enregistrés:")
        print("\tNom des aliments:\n")
        
        index = 0
        for x in result_name:
            index += 1
            print("{} - {}".format(index, x))

        print("\n\tLien internet pour plus d'infos:\n")
        
        index = 0
        for x in result_link:
            index += 1
            print("{} - {}".format(index, x))
        print("-------------------------------------------------------------")

        if fonc.end(user):
            main()

        else:
            db.close()
            sys.exit()


main()
db.close()
