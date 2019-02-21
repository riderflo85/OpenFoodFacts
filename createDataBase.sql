CREATE DATABASE IF NOT EXISTS 'purbeurre';

USE 'purbeurre';

CREATE TABLE 'pb_aliments'
(
    'id_aliments' INT NOT NULL AUTO_INCREMENT,
    'aliment_categorie' VARCHAR(45) NOT NULL UNIQUE,
    'aliment_name' VARCHAR(45) NOT NULL UNIQUE,
    'aliment_shop' VARCHAR(45),
    'aliment_link' VARCHAR(120),
    PRIMARY KEY('id_aliments')
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE 'pb_favoris'
(
    'id_favoris' INT NOT NULL AUTO_INCREMENT,
    'favoris_aliment_idAliments' INT,
    PRIMARY KEY('id_favoris'),
    FOREIGN KEY('favoris_aliment_idAliments') REFERENCES 'pb_aliments'('id_aliments')
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE 'pb_users'
(
    'id_users' INT NOT NULL AUTO_INCREMENT,
    'user_name' VARCHAR(45) NOT NULL UNIQUE,
    'user_passwd' VARCHAR(65) NOT NULL,
    'user_favoris_idFavoris' INT,
    PRIMARY KEY('id_users'),
    FOREIGN KEY('user_favoris_idFavoris') REFERENCES 'pb_favoris'('id_favoris')
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;