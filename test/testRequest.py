#! /usr/bin python3
#conding: utf-8

import requests
import json


dico = {}
my_list = []
nb = 1

while nb <= 10:
    api = "https://fr.openfoodfacts.org/categorie/legumes-et-derives/"+str(nb)
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
                #my_list.append([x["product_name_fr"], x["nutrition_grade_fr"], x["url"]])
                dico[pn] = ng, nova, st, url          #my_list
        except:
            pass

    with open("Légumes.json", "w") as file:
        json.dump(dico, file, indent=4, ensure_ascii=False)
    nb += 1
