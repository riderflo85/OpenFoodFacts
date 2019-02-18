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
        
            <<Système>>: 1 - Connexion
                         2 - Création de compte
                      
            "User": Tape 1
                        -> User veut se connectez.

                <<Système>>: Renseigner votre identifiant:
                
                "User": Tape son identifiant
                
                    <<Système>>: Identifiant correct, merci de renseignez votre mot de passe:
                                (Le système vérifie si l'identifiant exist)
                
                        "User": Tape son mot de passe
                        
                            <<Système>>: Mot de passe valide, enregistrement du résultat de votre recherche...
                                        (Le système vérifie si le mot de passe est correct)
                            
                            
                            
        

    "User": Tape 2
                -> User veut retrouver ses aliments enregistrés.
