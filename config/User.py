#! /usr/bin python3
# conding: utf-8

import sys
from passlib.hash import pbkdf2_sha256
from getpass import getpass


class User():
    """Class user"""

    def __init__(self, select):
        """Builder that defines initialization variables"""

        self.select = select
        self.passwd = None
        self.rep = None
        self.tent = 0
        self.current_user = None
        self.user_id = None

    def choice(self):
        """Function that requires the user to enter a response"""

        self.rep = input(self.select)
        return self.rep

    def sign_in(self, db):
        """Function that allows the user to connect to his account"""

        print("\nVeuillez renseigner votre identifiant: ")
        self.choice()
        db.select_where("user_name", "pb_users", "user_name", self.rep)

        # Verifies if the identifier is present in the database
        if db.colect_data[0][0] == self.rep:
            self.current_user = db.colect_data[0][0]
            print("Identifiant correct,")
            print("merci de renseignez votre mot de passe:")

            # Compare the password entered as well as the password
            # saved in the database
            if self.__password(db, create=False):
                db.select_where("id_users", "pb_users", "user_name",
                    self.current_user)
                self.user_id = db.colect_data[0][0]
                print("Mot de passe correct")

        else:
            print("\nL'identifiant n'existe pas, merci de recommencer !")
            self.sign_in(db)

    def sign_up(self, db):
        """Function that allows the user to create an account"""

        print("\nVeuillez renseigner un identifiant pour votre compte: ")
        self.choice()
        db.select_where("user_name", "pb_users", "user_name", self.rep)

        if db.colect_data == []:
            print("Identifiant libre,")
            print("merci de renseignez un mot de passe:")

            if self.__password(db, create=True):
                values = "'{}', '{}'".format(self.rep, self.passwd)
                self.current_user = self.rep
                db.insert_data("pb_users", "user_name, user_passwd", values)
                db.select_where("id_users", "pb_users", "user_name",
                    self.current_user)
                self.user_id = db.colect_data[0][0]
                print("Identifiant créez avec succès :-)")

        else:
            print("\nIdentifiant déjà pris, merci d'en choisir un autre:")
            self.sign_up(db)

    def __password(self, db, create):
        """Protected function that asks to enter a password and hash"""

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
            db.select_where("user_passwd", "pb_users", "user_name", self.rep)

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
