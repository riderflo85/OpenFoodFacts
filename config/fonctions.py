#! /usr/bin python3
# conding: utf-8

import json
import requests
import os
import mysql.connector

# My module
from . import constants as const


def check(user, cond):

    if user.rep in cond:
        pass

    else:
        print("Mauvaise réponse")
        user.choice()
        check(user, cond)


def search(user, db):

    cond = []
    db.select_data("*", "pb_categories", where=None, cond=None, join=False)
    print("\nSélectionnez une catégorie :\n")

    for x in db.colect_data:
        print("{} - {}".format(x[0], x[1]))
        cond.append(str(x[0]))

    user.choice()
    check(user, cond)

    print("\nSélectionnez un aliment :\n")
    foo = int(user.rep)-1
    done = db.colect_data[foo][1]
    db.select_data("aliment_name", "pb_aliments", "aliment_categorie",
        done, False)
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

    db.select_data(data, "pb_aliments", where, done, False)
    print("\nAliment sélectionnez : {}".format(db.colect_data[0][0]))
    db.result = db.colect_data[0][0]
    print("\nBoutique : {}".format(db.colect_data[0][1]))
    print("\nLien internet : {}\n".format(db.colect_data[0][2]))


def end(user):

    print("\nChoisissez une option: [1 ou 2]\n")
    print("1- {}\n2- {}".format(const.QUESTIONS[6], const.QUESTIONS[7]))
    user.choice()
    check(user, const.REP1)

    if user.rep == "1":
        return True

    else:
        return False


def pull_data():

    directory = os.path.dirname(__file__)
    folder = "../ressources/"
    food_file = os.path.join(directory, folder, "all.json")
    dico = {}

    for cat in const.CATEGORIES:
        page = 1
        my_list = []
        print(cat)

        while page <= 30:
            api = "https://fr.openfoodfacts.org/categorie/{}/{}"
            api = api.format(cat, str(page))
            payload = {"json": 1}
            r = requests.get(url=api, params=payload)
            print(r.url)

            try:
                rep = r.json()

            except json.decoder.JSONDecodeError:
                pass

            for x in rep["products"]:
                try:
                    pn = x["product_name_fr"].replace("\n", " ")
                    ng = x["nutrition_grade_fr"]
                    nova = x["nova_groups"]
                    st = x["stores_tags"]
                    url = x["url"]
                    if pn!="" and ng!="" and nova!="" and st!="" and url!="":
                        my_list.append([pn, ng, nova, st, url])
                        dico[cat] = my_list

                except:
                    pass

            page += 1

    with open(food_file, "w") as file:
        json.dump(dico, file, indent=4, ensure_ascii=False)


def push_data(db):

    directory = os.path.dirname(__file__)
    folder = "../ressources/"
    food_file = os.path.join(directory, folder, "all.json")

    with open(food_file, "r") as file:
        data = json.load(file)

    print("\n---------- Transfert des données en cours ----------\n")
    print("-> Ceci peut prendre plusieurs minutes, merci de patienter")

    for foo in data:
        categories = foo
        values = "'{}'".format(foo)
        db.insert_data("pb_categories", "categorie_name", values)

        for x in data[categories]:
            al_na = x[0]
            al_ca = categories
            al_nu = str(x[1])
            al_no = x[2]
            al_sh = x[3]
            al_li = x[4]
            ali_champs = "aliment_name, aliment_categorie, aliment_nutrition,\
 aliment_nova_group, aliment_shop, aliment_link"
            values = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\""
            values = values.format(al_na, al_ca, al_nu, al_no, al_sh, al_li)

            try:
                db.insert_data("pb_aliments", ali_champs, values)

            except mysql.connector.errors.IntegrityError:
                pass

    print("\n---------- Transfert terminé ------------------\n")


def delete_duplicates():

    """ Fonction de tri de données. Supprime les doublons présent dans un fichier
    .json"""

    directory = os.path.dirname(__file__)
    folder = "../ressources/"
    food_file = os.path.join(directory, folder, "all.json")

    list_sort = []
    temp = []
    all_temp = []
    dico = {}

    name_cate = ["boissons", "fruits", "legumes-et-derives",
    "produits-laitiers", "poissons", "viandes", "desserts",
    "cereales-et-derives"]

    with open(food_file, "r") as file:
        data = json.load(file)

        # On parcours chaque catégories d'aliments
        for cat in name_cate:

            for food_list in data[cat]:
                # Chaque aliment de la catégorie est ajouter a la liste de tri
                list_sort.append(food_list)

            index = -1

            # On parcours la liste d'aliment qui peut potentiellement contenir
            # des doublons
            for x in list_sort[:]:
                index += 1

                # Si l'aliment actuel n'est pas dans la liste temporaire on
                # l'ajoute
                if x[0].lower() not in temp and x[0].lower() not in all_temp:
                    temp.append(x[0].lower())
                    all_temp.append(x[0].lower())

                # Si l'aliment actuel est déjà dans la liste temporaire cela
                # veut dire que l'aliment actuel est un doublon, donc on le
                # supprime de sa liste grâce à son index
                else:
                    del(list_sort[index])
                    index -= 1

            # On ajoute le nom de la catégorie actuel ainsi que tout ses
            # aliments triés dans un dictionnaire
            dico[cat] = list_sort

            # On vide le contenu des deux listes pour pouvoir refaire la même
            # opération pour la catégorie suivante
            list_sort = []
            temp = []

    all_temp = []

    with open(food_file, "w") as file:
        json.dump(dico, file, indent=4, ensure_ascii=False)
