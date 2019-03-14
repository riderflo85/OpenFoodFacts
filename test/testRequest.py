#! /usr/bin python3
# conding: utf-8

import requests
import json
import sys
sys.path.append("..")
from config.DataBase import DataBase

dico = {}
db = DataBase("distant")

categories = ["boissons", "fruits", "legumes-et-derives", "produits-laitiers",
"poissons", "viandes", "desserts", "cereales-et-derives"]

for cat in categories:
    nb = 1
    my_list = []
    print(cat)
    while nb <= 30:
        api = "https://fr.openfoodfacts.org/categorie/{}/{}"
        api = api.format(cat, str(nb))
        payload = {"json": 1}
        r = requests.get(url=api, params=payload)
        print(r.url)
        rep = r.json()

        for x in rep["products"]:

            try:
                pn = x["product_name_fr"]
                ng = x["nutrition_grade_fr"]
                nova = x["nova_groups"]
                st = x["stores_tags"]
                url = x["url"]
                if pn != "" and ng != "" and nova != "" and st != "" and url != "":
                    my_list.append([pn, ng, nova, st, url])
                    dico[cat] = my_list
            except:
                pass
        nb += 1

with open("all.json", "w") as file:
            json.dump(dico, file, indent=4, ensure_ascii=False)
