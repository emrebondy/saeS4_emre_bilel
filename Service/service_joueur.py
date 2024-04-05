import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
from client_mongo import Client2Mongo
from DTO.joueur_dto import JoueurDTO

def rechercher_joueur(pseudo):
    donnees_joueur = Client2Mongo.collection_joueurs().find_one({"pseudo" : pseudo})
    joueur = JoueurDTO(
        nom=donnees_joueur.get("nom"),
        prenom=donnees_joueur.get("prenom"),
        pseudo=donnees_joueur.get("pseudo"),
        age=donnees_joueur.get("age"),
        niveau=donnees_joueur.get("niveau"),
        email=donnees_joueur.get("email"),
    )
    joueur.set_id(donnees_joueur.get("_id"))
    return joueur

def rechercher_joueur_par_id(id_joueur):
    donnees_joueur = Client2Mongo.collection_joueurs().find_one({"_id": id_joueur})
    if donnees_joueur:
        joueur = JoueurDTO(
            nom=donnees_joueur.get("nom"),
            prenom=donnees_joueur.get("prenom"),
            pseudo=donnees_joueur.get("pseudo"),
            age=donnees_joueur.get("age"),
            niveau=donnees_joueur.get("niveau"),
            email=donnees_joueur.get("email"),
        )
        joueur.set_id(donnees_joueur.get("_id"))
        return joueur

def creer_joueur(nom, prenom,pseudo, age, niveau, email):
    pseudo_exist = Client2Mongo.collection_joueurs().find_one({"pseudo": pseudo})

    if pseudo_exist :
        raise ValueError("Ce pseudo existe déjà !!!")
    
    if condition_joueur(nom,prenom,age,email):
        joueur = JoueurDTO(nom, prenom, pseudo, age, niveau, email)
        Client2Mongo.collection_joueurs().insert_one(joueur.__dict__) 
        return joueur
    

def condition_joueur(nom,prenom,age,email):
    if not nom.isalpha():
        raise ValueError("Le nom ne doit contenir que des lettres alphabétiques")
    if not prenom.isalpha():
        raise ValueError("Le prénom ne doit contenir que des lettres alphabétiques")
    if not 18 <= age <= 99:
        raise ValueError("L'âge doit être un entier compris entre 18 et 99")
    if email is not None and '@' not in email:
        raise ValueError("L'adresse email doit contenir un '@'")
    return True

def supprimer_joueur(pseudo):
    joueur = rechercher_joueur(pseudo)
    Client2Mongo.collection_joueurs().delete_one({"pseudo": joueur.get_pseudo()})
    return joueur

def get_joueurs():
    joueurs_cursor = Client2Mongo.collection_joueurs().find()  
    joueurs_list = []

    for joueur in joueurs_cursor:
        joueur_dto = JoueurDTO(
            nom=joueur.get("nom"),
            prenom=joueur.get("prenom"),
            pseudo=joueur.get("pseudo"),
            age=joueur.get("age"),
            niveau=joueur.get("niveau"),
            email=joueur.get("email")
        )
        joueur_dto.set_id(joueur.get("_id"))
        joueurs_list.append(joueur_dto)

    return joueurs_list

def modifier_joueur(pseudo, nouveau_nom, nouveau_prenom, nouveau_pseudo, nouveau_age, nouveau_niveau, nouveau_mail):
    joueur_existant = Client2Mongo.collection_joueurs().find_one({"pseudo": nouveau_pseudo})
    
    if joueur_existant and joueur_existant["pseudo"] != pseudo:
        raise ValueError("Le nouveau pseudo est déjà utilisé par un autre joueur.")
    
    if condition_joueur(nouveau_nom, nouveau_prenom, nouveau_age, nouveau_mail):    
        update_data = {}
        if nouveau_nom:
            update_data["nom"] = nouveau_nom
        if nouveau_prenom:
            update_data["prenom"] = nouveau_prenom
        if nouveau_pseudo:
            update_data["pseudo"] = nouveau_pseudo
        if nouveau_age:
            update_data["age"] = nouveau_age
        if nouveau_niveau:
            update_data["niveau"] = nouveau_niveau
        if nouveau_mail:
            update_data["email"] = nouveau_mail
        
        Client2Mongo.collection_joueurs().update_one({"pseudo": pseudo}, {"$set": update_data})

        return rechercher_joueur(nouveau_pseudo);    
