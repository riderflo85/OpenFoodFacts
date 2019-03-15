#! /usr/bin python3
# conding: utf-8

import requests
import json
import sys
sys.path.append("..")
from config.DataBase import DataBase
from config import constants as const


db = DataBase("purbeurre")

def pull_data():
    dico = {}
    for cat in const.CATEGORIES:
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
                    if pn!="" and ng!="" and nova!="" and st!="" and url!="":
                        my_list.append([pn, ng, nova, st, url])
                        dico[cat] = my_list
                except:
                    pass
            nb += 1

    with open(const.FOODFILE, "w") as file:
                json.dump(dico, file, indent=4, ensure_ascii=False)

def push_data(db):
    with open(const.FOODFILE, "r") as file:
        data = json.load(file)

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
            values = "'{}','{}','{}','{}','{}','{}'"
            values = values.format(al_na, al_ca, al_nu, al_no, al_sh, al_li)
            db.insert_data("pb_aliments", ali_champs, values)
