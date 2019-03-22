   ### CONTEXTE

D'après une étude réalisée sur l'alimentation des français, notre équipe a remarqué que tout le monde souhaite changer son alimentation mais ne sais
pas par quoi commencer. Remplacer le Nutella par une pâte aux noisettes, oui, mais laqeulle? Et dans magasin l'acheter?
Notre équipe de développeur a eu l'idée de créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments, les comparer
et vous proposez un substitut plus sain à l'aliment qui vous fait envie.


   ### FONCTIONNALITÉS UTILISATEUR

    - L'utilisateur choisi entre remplacer un aliment ou consulter ses favoris (ses aliments substitués):

    Remplacer un aliment:
        - L'utilisateur sélectionne une catégorie d'aliments
        - L'utilisateur sélectionne un aliment de la catégorie
        - L'utilisateur choisi entre enregistrer le résultat dans une base de données ou effectuer une nouvelle recherche

            Enregistrer le résultat:
                - L'utilisateur choisi entre Connexion ou Création de compte

                    Connexion:
                        - L'utilisateur renseigne son identifiant
                        - L'utilisateur renseigne son mot de passe
                        - L'utilisateur peut quittez le programme ou faire une nouvelle recherche

                    Création de compte:
                        - L'utilisateur renseigne un identifiant
                        - L'utilisateur renseigne un mot de passe
                        - L'utilisateur peut quittez le programme ou faire une nouvelle recherche


    Consulter ses favoris:

        Connexion:
             - L'utilisateur renseigne son identifiant
             - L'utilisateur renseigne son mot de passe
             - L'utilisateur peut quittez le programme ou faire une nouvelle recherche

  ### PRÉ-REQUIS

    - Python3.7
    - Pipenv (pip3 install pipenv)
    - MySql


  ### INSTALLATION

    Une fois python3.7 et mysql installés, créez un utilisateur mysql et attribuer les droits sur la base de données 'purbeurre'

        - CREATE USER 'user'@'hôte' IDENTIFIED BY 'mot_de_passe';
        - GRANT ALL PRIVILEGES ON purbeurre.* TO 'user'@'hôte';


    Ensuite, téléchargez ou clonez le dépôt, déplacez-vous dans le dossier du projet et installez les dépendances

        - pipenv install


    Éditez le fichier "constants.py" et précisez l'hôte(HOST), le nom d'utilisateur(USER) ainsi que le mot de passe(PWD) de l'utilisateur précédement créé dans mysql


    Puis lancez le script "createDB.py"

        - python3 createDB.py

  ### UTILISATION

    Vous pouvez maintenant executer "main.py"
