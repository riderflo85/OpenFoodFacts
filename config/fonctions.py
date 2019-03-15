#! /usr/bin python3
# conding: utf-8

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
