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
             
             
   ### DÉROULEMENT DU PROGRAMME
    
    <<Système>>: 1 - Quel aliment souhaitez-vous remplacer?
                 2 - Retrouver mes aliments substitués.
             
    "User": Tape 1
                -> User veut remplacer un aliment

        <<Système>>: Sélectionnez la catégorie.
                    (Affichage des catégories (Chaque catégorie est associées à un chiffre))
            
        "User": Tape le chiffre associé à la catégorie voulu.
                    -> User choisi une catégorie
            
        <<Système>>: Sélectionner l'aliment.
                    (Affichage des aliments (Chaque catégorie est associées à un chiffre))
            
        "User": Tape le chiffre associé à l'aliment voulu.
                    -> User choisi un aliment

        <<Système>>: Voici un substitut à l'aliment {aliment}
            Description: {description_aliment}
            Magasin: {shop}
            Lien: {link}
    
        <<Système>>: Voulez-vous enregistrer le résultat? (O/N)

        "User": Tape O
                    -> User veut enregristrer le résultat
        
            <<Système>>: 1 - Connexion
                         2 - Création de compte
                      
            "User": Tape 1
                        -> User veut se connectez.

                <<Système>>: Veuillez renseigner votre identifiant:
                
                "User": Tape son identifiant
                
                    <<Système>>: Identifiant correct, merci de renseignez votre mot de passe:
                                (Le système vérifie si l'identifiant exist)
                
                        "User": Tape son mot de passe
                        
                            <<Système>>: Mot de passe valide, enregistrement du résultat de votre recherche...
                                        (Le système vérifie si le mot de passe est correct)
                                        (Le programme recommence au début (question 1))

                            <<Système>>: Mot de passe incorrect, veuillez re-commencer (tentavtie 1/3)
                                        (Le système vérifie si le mot de passe est correct)
                            
                                <<Système>>: Vous avez fait trois tentatives sans succès, le résultat ne sera pas enregistré.
                                            (Le système n'enregistre pas le résultat et recommence au début (question 1))

            "User": Tape 2
                        -> User veut se créer un compte
            
                <<Système>>: Veuillez renseigner un identifiant pour votre compte:

                "User": Renseigne un identifiant
                            (Le système vérifie si l'identifiant existe ou pas)

                    <<Système>>: L'identifiant existe déjà, veuillez en renseigner un autre
                                (Le système vérifie si l'identifiant existe ou pas, si il existe il répete la question)
                
                <<Système>>: Veuillez renseigner un mot de passe:

                "User": Renseigne un mot de passe

                <<Système>>: Votre compte à bien été créé, votre résultat de recherche est enregistrer
                            (Le système créé le compte et enregistre le résultat de la recherche dans la base de données)

                <<Système>>: 1 - Quittez le programme
                             2 - Faire une nouvelle recherche

                "User": Tape 1
                            -> User veut quittez le programme.

                    <<Système>>: Vous quittez le programme, à bientôt
                                (Le système ferme le programme)
                
                "User": Tape 2
                            -> User veut effectuer une nouvelle recherche

                    <<Système>>: (Le système recommence au début (question 1))

        "User": Tape N
                    -> User ne veut pas enregistrer le résultat de sa recherche
            
            <<Système>>: 1 - Quittez le programme
                         2 - Faire une nouvelle recherche
                            
            "User": Tape 1
                        -> User veut quittez le programme.

                <<Système>>: Vous quittez le programme, à bientôt
                            (Le système ferme le programme)

            "User": Tape 2
                        -> User veut effectuer une nouvelle recherche

                <<Système>>: (Le système recommence au début (question 1))
        

    "User": Tape 2
                -> User veut retrouver ses aliments enregistrés.

        <<Système>>: Veuillez renseigner votre identifiant:

        "User": Tape son identifiant
                
            <<Système>>: Identifiant correct, merci de renseignez votre mot de passe:
                        (Le système vérifie si l'identifiant exist)
            
                "User": Tape son mot de passe
                    
                    <<Système>>: Mot de passe valide
                                (Le système vérifie si le mot de passe est correct)
                        
                        <<Système>>: Aliment cherché: {liste d'aliments cherchés}
                                     Substitut enregistrés: {liste de subtitut enregistrés}

                    <<Système>>: Mot de passe incorrect, veuillez re-commencer (tentavtie 1/3)
                                (Le système vérifie si le mot de passe est correct)
                        
                        <<Système>>: Vous avez fait trois tentatives sans succès, vos favoris ne sont pas accessible.
                                    (Le système n'affiche pas les favoris et recommence au début (question 1))

                    <<Système>>: 1 - Quittez le programme
                                 2 - Faire une nouvelle recherche

                    "User": Tape 1
                                -> User veut quitter le programme

                        <<Système>>: Vous quittez le programme, à bientôt
                                    (Le système quitte le programme)

                    "User": Tape 2
                                -> User veut faire une nouvelle recherche
                    
                        <<Système>>: (Le système recommence au début (question 1))

            <<Système>>: Identifiant incorrect, aucun compte ne correspond à cette identifiant.

                <<Système>>: 1 - Créer un compte
                             2 - Faire une nouvelle recherche
                             3 - Quittez le programme

                    "User": Tape 1
                    
                        <<Système>>: (Le système renvoi à la création de compte)

                    "User": Tape 2

                        <<Système>>: (Le système recommence au début (question 1))

                    "User": Tape 3

                        <<Système>>: Vous quittez le programme, à bientôt
                                    (Le système quitte le programme)

