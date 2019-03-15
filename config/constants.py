#! /usr/bin python3
# conding: utf-8

API = "https://fr.openfoodfacts.org/cgi/search.pl"

# -----------------------DataBase----------------------------------------------
HOST = "192.168.1.13"
USER = "distant"
PWD = "test"
# -----------------------------------------------------------------------------

FOODFILE = "../ressources/all.json"

USERCHOICE = ">>> "

CATEGORIES = ["boissons", "fruits", "legumes-et-derives", "produits-laitiers",
"poissons", "viandes", "desserts", "cereales-et-derives"]

QUESTIONS = {
    1: "Quel aliment souhaitez-vous remplacer ?",
    2: "Retrouver mes aliments substitués.",
    3: "Selectionnez la catégorie:",
    4: "Sélectionnez l'aliment:",
    5: "Voulez-vous enregistrer le résultat? [O/N]",
    6: "Faire une nouvelle recherche",
    7: "Quittez le programme"
}

REP1 = ["1", "2"]
REP = ["o", "O", "n", "N"]
