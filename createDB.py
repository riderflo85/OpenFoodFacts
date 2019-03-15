#! /usr/bin python3
# conding: utf-8

import mysql.connector

# My module
from config import constants as const

conn = mysql.connector.connect(
    hosts=const.HOST,
    user=const.USER,
    passwd=const.PWD,
    database="purbeurre"
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
