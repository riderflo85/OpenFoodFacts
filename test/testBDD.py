#! /usr/bin python3
#conding: utf-8

import mysql.connector

class Data_base():

    def __init__(self, name_BDD):
        self.name_BDD = name_BDD
        self.conn = None
        self.cursor = None

    def connexion(self, host, user, passwd):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=self.name_BDD
        )
        self.cursor = self.conn.cursor()
        return self.cursor
    
my_BDD = Data_base("testDist")

my_BDD.connexion("192.168.1.13", "distant", "test")
print("Connecter !!!")

#----------------CRÉER UNE TABLE-------------------------------------
insert_table = (
    """CREATE TABLE IF NOT EXISTS voiture (
        id SMALLINT(6) NOT NULL AUTO_INCREMENT UNSIGNED,
        marque VARCHAR(12) NOT NULL,
        type_carburant VARCHAR(7),
        puissance SMALLINT(4),
        PRIMARY KEY(id)
        );
""")
#--------------------------------------------------------------------

#----------------INÉRER DES DONNÉES----------------------------------
insert_data = (
    """INSERT INTO voiture (marque, type_carburant, puissance)
    VALUES (%s, %s, %s);"""
)

data = ('AUDI', 'essence', 850)

my_BDD.cursor.execute(insert_data, data)

# Pour enregistrer et validé les changements dans la BDD TRÈS IMPORTANT !!!!!!!
my_BDD.conn.commit()
print("Attribution de données, réussi")
#--------------------------------------------------------------------


#----------------RÉCUPERER DES DONNÉES-------------------------------
my_BDD.cursor.execute("SELECT * FROM voiture")
colect_data = my_BDD.cursor.fetchall()
print(colect_data)
#--------------------------------------------------------------------

my_BDD.conn.close()