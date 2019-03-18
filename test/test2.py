#! /usr/bin python3
#conding: utf-8

import json
# Fonction de tri de données. Supprime les doublons présent dans un fichier
# .json

def delete_duplicates():
    """ Fonction de tri de données. Supprime les doublons présent dans un fichier
    .json"""

    list_sort = []
    temp = []
    dico = {}

    name_cate = ["boissons", "fruits", "legumes-et-derives", "produits-laitiers",
    "poissons", "viandes", "desserts", "cereales-et-derives"]

    with open("all.json", "r") as file:
        data = json.load(file)

        # On parcours chaque catégories d'aliments
        for cat in name_cate:

            for food_list in data[cat]:
                # Chaque aliment de la catégorie est ajouter a la liste de tri
                list_sort.append(food_list)

            print(len(list_sort))
            index = -1

            # On parcours la liste d'aliment qui peut potentiellement contenir
            # des doublons
            for x in list_sort[:]:
                index += 1

                # Si l'aliment actuel n'est pas dans la liste temporaire on
                # l'ajoute
                if x[0] not in temp:
                    temp.append(x[0])

                # Si l'aliment actuel est déjà dans la liste temporaire cela
                # veut dire que l'aliment actuel est un doublon, donc on le
                # supprime de sa liste grâce à son index
                else:
                    del(list_sort[index])
                    index -= 1

            # On ajoute le nom de la catégorie actuel ainsi que tout ses aliments
            # triés dans un dictionnaire
            dico[cat] = list_sort
            print(len(list_sort))

            # On vide le contenu des deux listes pour pouvoir refaire la même
            # opération pour la catégorie suivante
            list_sort = []
            temp = []


    with open("all.json", "w") as file:
        json.dump(dico, file, indent=4, ensure_ascii=False)