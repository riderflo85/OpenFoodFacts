#! /usr/bin python3
# conding: utf-8


# -----------------------DataBase----------------------------------------------
HOST = "192.168.1.13"
USER = "distant"
PWD = "test"
# -----------------------------------------------------------------------------

FOODFILE = "../ressources/all.json"

USERCHOICE = ">>> "

CATEGORIES = ["boissons", "cereales-et-derives", "desserts", "fruits",
"legumes-et-derives", "poissons", "produits-laitiers", "viandes"]

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

INFOS_GN = "\tClassification NOVA pour la transformation des aliments;\n\
Une classification en 4 groupes pour mettre en évidence le degré de transformation des aliments\n\
Groupe 1 - Aliments non transformés ou transformés minimalement\n\
Groupe 2 - Ingrédients culinaires transformés\n\
Groupe 3 - Aliments transformés\n\
Groupe 4 - Produits alimentaires et boissons ultra-transformés"