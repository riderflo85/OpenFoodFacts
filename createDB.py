#! /usr/bin python3
# conding: utf-8

import mysql.connector

# My module
from config import constants as const
from config import fonctions as fonc
from config.DataBase import DataBase


def create_db():
    conn = mysql.connector.connect(
        host=const.HOST,
        user=const.USER,
        passwd=const.PWD
    )
    cursor = conn.cursor()

    request = []
    with open("ressources/database.sql", "r") as file:
        data = file.readlines()

        for x in data:
            request.append(x.rstrip("\n"))

        for req in request:
            cursor.execute(req)
            conn.commit()

    conn.close()


def main():
    db = DataBase("purbeurre")
    db.connexion(const.HOST, const.USER, const.PWD)
    fonc.pull_data()
    fonc.delete_duplicates()
    fonc.push_data(db)
    db.close()

create_db()
main()
