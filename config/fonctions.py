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
