#! /usr/bin python3
# conding: utf-8

import mysql.connector


class DataBase():

    def __init__(self, name_BDD):
        self.name_BDD = name_BDD
        self.conn = None
        self.cursor = None
        self.colect_data = None
        self.result = None

    def connexion(self, host, user, passwd):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=self.name_BDD
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, *args):
        req = "INSERT INTO {} ({}) VALUES ({});".format(*args)
        self.__execute(req)
        self.__commit()

    def select_data(self, donnees, table, where, cond, join, *args):
        if where is None and cond is None and join is False:
            req = "SELECT {} FROM {}".format(donnees, table)
            self.__execute(req)
            self.colect_data = self.cursor.fetchall()

        elif where is None and cond is None and join:
            req = "SELECT {} from {} inner join {} on {}={};"
            req = req.format(donnees, table, *args)
            self.__execute(req)
            self.colect_data = self.cursor.fetchall()

        elif join:
            req = "SELECT {} from {} inner join {} on {}={} where {}={};"
            req = req.format(donnees, table, *args, where, cond)
            self.__execute(req)
            self.colect_data = self.cursor.fetchall()

        else:
            req = "SELECT {} FROM {} WHERE {} = '{}'"
            req = req.format(donnees, table, where, cond)
            self.__execute(req)
            self.colect_data = self.cursor.fetchall()

    def close(self):
        self.conn.close()

    def __execute(self, *args):
        self.cursor.execute(*args)

    def __commit(self):
        self.conn.commit()
