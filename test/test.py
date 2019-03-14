#! /usr/bin python3
#conding: utf-8

import mysql.connector
import json

class DataBase():

    def __init__(self, name_BDD):
        self.name_BDD = name_BDD
        self.conn = None
        self.cursor = None
        self.colect_data = None

    def connexion(self, host, user, pwd):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=pwd,
            database=self.name_BDD
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, *args):
        req = "INSERT INTO {} ({}) VALUES ({});".format(*args)
        #import pdb; pdb.set_trace()
        self.__execute(req)
        self.__commit()

    def select_data(self, donnee, table, where, cond, join, *args):

        if where == None and cond == None:
            req1 = "SELECT {} FROM {}".format(donnee, table)
            self.__execute(req1)
            self.colect_data = self.cursor.fetchall()

        elif join:
            req2 = "SELECT {} from {} inner join {} on {}={} where {}={};"
            req2 = req2.format(donnee, table, *args, where, cond)
            self.__execute(req2)
            self.colect_data = self.cursor.fetchall()

        else:
            req = "SELECT {} FROM {} WHERE {} = '{}'"
            req = req.format(donnee, table, where, cond)
            self.__execute(req)
            self.colect_data = self.cursor.fetchall()

    def close(self):
        self.conn.close()
    
    def __execute(self, *args):
        self.cursor.execute(*args)
    
    def __commit(self):
        self.conn.commit()
    

def main():
    db = DataBase("purbeurre")
    db.connexion("192.168.1.13", "distant", "test")

    #------Insertion de catégories--------------------------------------------
    #cat = []
    #with open('familles-alimentaire.json', 'r') as file:
    #    data = json.load(file)
    #    for x in data.values():
    #        cat.append(x)

    #name_cat = sorted(cat)
    #for x in name_cat:
    #    db.insert_data("pb_categories", "categorie_name", x)
    #-------------------------------------------------------------------------

    #------Insertion d'aliments-----------------------------------------------
    #with open('aliments.json', 'r') as file:
    #    data = json.load(file)

    #    for x in data["aliments"]:
    #        #import pdb; pdb.set_trace()
    #        ali_name = x["nom"]
    #        ali_categ = x["categorie"]
    #        ali_shop = x["boutique"]
    #        ali_lien = x["lien"]
    #        colonne = "aliment_categorie ,aliment_name, aliment_shop, aliment_link"
    #        value = "'{}', '{}', '{}', '{}'".format(ali_categ ,ali_name, ali_shop, ali_lien)
    #        db.insert_data("pb_aliments", colonne, value)

    #------Rédcupération de données-------------------------------------------
    argum = ["pb_favoris", "id_aliments", "favoris_aliment"]
    db.select_data("aliment_name", "pb_aliments", None, None, False)
    print(db.colect_data)
    #-------------------------------------------------------------------------
    db.close()

main()