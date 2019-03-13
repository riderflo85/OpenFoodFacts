#! /usr/bin python3
# conding: utf-8

import sys
from passlib.hash import pbkdf2_sha256
from getpass import getpass


class User():

    def __init__(self, select):
        self.select = select
        self.passwd = None
        self.rep = None
        self.tent = 0

    def choice(self):
        self.rep = input(self.select)
        return self.rep

    def sign_in(self, db):
        print("\nVeuillez renseigner votre identifiant: ")
        self.choice()
        db.select_data("user_name", "pb_users", "user_name", self.rep, False)

        if db.colect_data[0][0] == self.rep:
            print("Identifiant correct,")
            print("merci de renseignez votre mot de passe:")

            if self.__password(db, create=False):
                print("Mot de passe correct")

        else:
            print("\nL'identifiant n'existe pas, merci de recommencer !")
            self.sign_in(db)

    def sign_up(self, db):
        print("\nVeuillez renseigner un identifiant pour votre compte: ")
        self.choice()
        db.select_data("user_name", "pb_users", "user_name", self.rep, False)

        if db.colect_data == []:
            print("Identifiant libre,")
            print("merci de renseignez un mot de passe:")

            if self.__password(db, create=True):
                values = "'{}', '{}'".format(self.rep, self.passwd)
                db.insert_data("pb_users", "user_name, user_passwd", values)
                print("Identifiant créez avec succès :-)")

        else:
            print("\nIdentifiant déjà pris, merci d'en choisir un autre:")
            self.sign_up(db)

    def __password(self, db, create):
        if create:
            pwd = getpass()
            hashed = pbkdf2_sha256.hash(pwd)

            if pbkdf2_sha256.verify(pwd, hashed):
                self.passwd = hashed
                return True

            else:
                return False

        else:
            pwd = getpass()
            db.select_data("user_passwd", "pb_users", "user_name",
                self.rep, False)

            if pbkdf2_sha256.verify(pwd, db.colect_data[0][0]):
                return True

            else:
                self.tent += 1
                print("Mot de passe incorrect, tentative {}/3"
                    .format(self.tent))

                if self.tent == 3:
                    return False
                    sys.exit()

                else:
                    self.__password(db, create=False)
