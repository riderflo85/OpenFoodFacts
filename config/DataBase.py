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
        self.food_search = None
        self.substi = None

    def connexion(self, host, user, passwd):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=self.name_BDD
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, one, *args):
        if one:
            req = "INSERT INTO {} ({}) VALUES ({});".format(*args)
            self.__execute(req)
            self.__commit()

        else:
            req = "INSERT INTO {} ({}) VALUES ({}), ({});".format(*args)
            self.__execute(req)
            self.__commit()

    def select_simple(self, data, table):
        req = "SELECT {} FROM {}".format(data, table)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()

    def select_join(self, data, table, *args):
        req = "SELECT {} FROM {} INNER JOIN {} ON {}={};"
        req = req.format(data, table, *args)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()

    def select_where(self, data, table, where, cond):
        req = "SELECT {} FROM {} WHERE {} = \"{}\""
        req = req.format(data, table, where, cond)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()

    def select_where_join(self, data, table, where, cond, *args):
        req = "SELECT {} FROM {} INNER JOIN {} ON {}={} WHERE {}={};"
        req = req.format(data, table, *args, where, cond)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()
    
    def select_where_and(self, data, table, where, cond, c1, v1, c2, v2):
        req = "SELECT {} FROM {} WHERE {}='{}' AND {} < '{}' AND {} < {};"
        req = req.format(data, table, where, cond, c1, v1, c2, v2)
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()
    
    def union(self, d1, t1, w1, cond1, d2, t2, w2, cond2):
        req1 = "SELECT {} FROM {} WHERE {} = \"{}\" UNION "
        req1 = req1.format(d1, t1, w1, cond1)
        req2 = "SELECT {} FROM {} WHERE {} = \"{}\";"
        req2 = req2.format(d2, t2, w2, cond2)
        req = req1+req2
        self.__execute(req)
        self.colect_data = self.cursor.fetchall()

    def update(self, table, column, data, where, cond):
        req = "UPDATE {} SET {} = '{}' WHERE {} = '{}';"
        req = req.format(table, column, data, where, cond)
        self.__execute(req)
        self.__commit()

    def close(self):
        self.conn.close()

    def __execute(self, *args):
        self.cursor.execute(*args)

    def __commit(self):
        self.conn.commit()
