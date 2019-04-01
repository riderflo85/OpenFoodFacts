#! /usr/bin python3
# conding: utf-8

import mysql.connector


class DataBase():
    """Classe qui gère les requetes SQL avec la base de données"""

    def __init__(self, name_BDD):
        """Constructeur de la classe qui défini des variables de base"""

        self.name_BDD = name_BDD
        self.conn = None
        self.cursor = None
        self.colect_data = None
        self.result = None
        self.food_search = None
        self.substi = None

    def connexion(self, host, user, passwd):
        """Connexion à la base de données"""

        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=self.name_BDD
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, *args):
        """Insertion de données"""

        req = "INSERT INTO {} ({}) VALUES ({});".format(*args)
        self.__execute(req)
        self.__commit()

    def select_simple(self, data, table):
        """Selection simple de donnée"""

        req = "SELECT {} FROM {}".format(data, table)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()

    def select_join(self, data, table, *args):
        """Sélection de données avec une jointure"""

        req = "SELECT {} FROM {} INNER JOIN {} ON {}={};"
        req = req.format(data, table, *args)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()

    def select_where(self, data, table, where, cond):
        """Sélection de donnée avec une clause where"""

        req = "SELECT {} FROM {} WHERE {} = \"{}\""
        req = req.format(data, table, where, cond)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()

    def select_where_join(self, data, table, where, cond, *args):
        """Sélection de donnée avec une jointure et une clause where"""

        req = "SELECT {} FROM {} INNER JOIN {} ON {}={} WHERE {}={};"
        req = req.format(data, table, *args, where, cond)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()
    
    def select_where_and(self, data, table, where, cond, c1, v1, c2, v2):
        """Sélection de donnée multiple avec une clause where"""

        req = "SELECT {} FROM {} WHERE {}='{}' AND {} < '{}' AND {} < {};"
        req = req.format(data, table, where, cond, c1, v1, c2, v2)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()
    
    def union(self, d1, t1, w1, cond1, d2, t2, w2, cond2):
        """Union de requetes avec la clause where"""

        req1 = "SELECT {} FROM {} WHERE {} = \"{}\" UNION "
        req1 = req1.format(d1, t1, w1, cond1)
        req2 = "SELECT {} FROM {} WHERE {} = \"{}\";"
        req2 = req2.format(d2, t2, w2, cond2)
        req = req1+req2
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()

    def close(self):
        """Fermeture de la connexion avec la base de données"""

        self.conn.close()

    def __execute(self, *args):
        """Méthode de classe protégéé qui permet de d'executé les requetes
        SQL"""

        self.cursor.execute(*args)

    def __commit(self):
        """Méthode de classe protégée qui permet de validé l'insertion de
        données dans la base de données"""

        self.conn.commit()
