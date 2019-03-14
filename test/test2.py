#! /usr/bin python3
#conding: utf-8

import json


with open("BoissonsPage1.json", "r") as file:
    data = json.load(file)
    foo = data["product"]
    print(foo[0])           # -> ['Apfelschorle', 'https://fr.openfoodfacts.org/produit/4311596435821/apfelschorle-gut-gunstig']
    print(foo[0][0])        # -> Apfelschorle
    print(foo[0][1])        # -> https://fr.openfoodfacts.org/produit/4311596435821/apfelschorle-gut-gunstig