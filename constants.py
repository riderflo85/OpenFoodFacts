#! /usr/bin python3
#conding: utf-8

API = "https://fr.openfoodfacts.org/cgi/search.pl"

#-----------------------DataBase----------------------------------------------
HOST = "192.168.1.13"
USER = "distant"
PWD = "test"
#-----------------------------------------------------------------------------

USERCHOICE = ">>> "

CATEGORIES = {
    1: "Boissons",
    2: "Fruits",
    3: "Légumes",
    4: "Céréales",
    5: "Féculents",
    6: "Produits laitiers",
    7: "Viande",
    8: "Poisson",
    9: "Oeuf",
    10: "Corps gras",
    11: "Sucre"
}

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