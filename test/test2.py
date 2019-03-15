#! /usr/bin python3
#conding: utf-8

import json


# categories = []

def insert_data(*args):
    req = "INSERT INTO {} ({}) VALUES ({});".format(*args)
    print(req)

with open("../ressources/all.json", "r") as file:
    data = json.load(file)

    for foo in data:
        categories = foo
        values = "'{}'".format(foo)
        insert_data("pb_categories", "categorie_name", values)
        for x in data[categories]:
            al_na = x[0]
            al_ca = categories
            al_nu = str(x[1])
            al_no = x[2]
            al_sh = x[3]
            al_li = x[4]
            ali_cat = "aliment_name, aliment_categorie, aliment_nutrition,\
 aliment_nova_group, aliment_shop, aliment_link"
            values = "'{}','{}','{}','{}','{}','{}'"
            values = values.format(al_na, al_ca, al_nu, al_no, al_sh, al_li)
            insert_data("pb_aliments", ali_cat, values)
            #print("{} | {} | {} | {} | {} | {}".format(al_na, al_ca, al_nu, al_no, al_sh, al_li))
