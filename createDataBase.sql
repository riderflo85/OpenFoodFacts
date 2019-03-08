CREATE DATABASE IF NOT EXISTS purbeurre;

USE purbeurre;

------------------------------------------------------------------------------
CREATE TABLE pb_categories
(
    id_categorie INT UNSIGNED NOT NULL AUTO_INCREMENT,
    categorie_name VARCHAR(45) NOT NULL UNIQUE,
    PRIMARY KEY(id_categorie)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
------------------------------------------------------------------------------

------------------------------------------------------------------------------
CREATE TABLE pb_aliments
(
    id_aliments INT UNSIGNED NOT NULL AUTO_INCREMENT,
    aliment_name VARCHAR(45) NOT NULL UNIQUE,
    aliment_categorie VARCHAR(45) NOT NULL,
    aliment_shop VARCHAR(45),
    aliment_link VARCHAR(120),
    PRIMARY KEY(id_aliments)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
------------------------------------------------------------------------------

------------------------------------------------------------------------------
CREATE TABLE pb_favoris
(
    id_favoris INT UNSIGNED NOT NULL AUTO_INCREMENT,
    favoris_aliment INT UNSIGNED,
    PRIMARY KEY(id_favoris)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
------------------------------------------------------------------------------

------------------------------------------------------------------------------
CREATE TABLE pb_users
(
    id_users INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(45) NOT NULL UNIQUE,
    user_passwd VARCHAR(88) NOT NULL,
    user_favoris INT UNSIGNED,
    PRIMARY KEY(id_users)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
------------------------------------------------------------------------------

-------Clé étrangère----------------------------------------------------------
ALTER TABLE pb_aliments
ADD CONSTRAINT FK_pb_aliments FOREIGN KEY(aliment_categorie) REFERENCES pb_categories(categorie_name);
ALTER TABLE pb_favoris
ADD CONSTRAINT FK_pb_favoris FOREIGN KEY(favoris_aliment) REFERENCES pb_aliments(id_aliments);
ALTER TABLE pb_users
ADD CONSTRAINT FK_pb_users FOREIGN KEY(user_favoris) REFERENCES pb_favoris(id_favoris);
------------------------------------------------------------------------------