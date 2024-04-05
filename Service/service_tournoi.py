import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
from client_mongo import Client2Mongo
from DTO.tournoi_dto import TournoiDTO
from Service.service_joueur import rechercher_joueur

def rechercher_tournoi(nom):
    donnees_tournoi = Client2Mongo.collection_tournois().find_one({"nom": nom})
    tournoi = TournoiDTO(
        nom=donnees_tournoi.get("nom"),
        date=donnees_tournoi.get("date"),
        duree=donnees_tournoi.get("duree"),
        lieu=donnees_tournoi.get("lieu"),
        list_joueur_dto=donnees_tournoi.get("list_joueur_dto"),
        list_match=donnees_tournoi.get("list_match"),
        pwd=donnees_tournoi.get("pwd"),
    )
    tournoi.set_id(donnees_tournoi.get("_id"))
    return tournoi

def rechercher_tournoi_id(_id):
    donnees_tournoi = Client2Mongo.collection_tournois().find_one({"_id": _id})
    tournoi = TournoiDTO(
        nom=donnees_tournoi.get("nom"),
        date=donnees_tournoi.get("date"),
        duree=donnees_tournoi.get("duree"),
        lieu=donnees_tournoi.get("lieu"),
        list_joueur_dto=donnees_tournoi.get("list_joueur_dto"),
        list_match=donnees_tournoi.get("list_match"),
        pwd=donnees_tournoi.get("pwd"),
    )
    tournoi.set_id(donnees_tournoi.get("_id"))
    return tournoi

def creer_tournoi(nom, date, duree, lieu, pwd):
    tournoi = TournoiDTO(nom, date, duree, lieu, list_joueur_dto=[], list_match=[], pwd=pwd)
        
    Client2Mongo.collection_tournois().insert_one(tournoi.__dict__)
        
    return tournoi

def inscrire_joueur_au_tournoi(pseudo, _id):
    tournoi = rechercher_tournoi(_id)
    joueur = rechercher_joueur(pseudo)

    if tournoi.get_list_joueur_dto():
        if joueur.get_id() in tournoi.get_list_joueur_dto():
            raise ValueError("Ce joueur est déjà inscrit au tournoi.")
    
    tournoi.add_joueur(joueur.get_id())
     
    Client2Mongo.collection_tournois().update_one({"_id": tournoi.get_id()}, {"$set": tournoi.__dict__})

    return tournoi

def get_tournois():
    tournois_cursor = Client2Mongo.collection_tournois().find()
    tournois_list = []

    for tournoi_data in tournois_cursor:
        tournoi = TournoiDTO(
            nom=tournoi_data.get("nom"),
            date=tournoi_data.get("date"),
            duree=tournoi_data.get("duree"),
            lieu=tournoi_data.get("lieu"),
            list_joueur_dto=tournoi_data.get("list_joueur_dto"),
            list_match=tournoi_data.get("list_match"),
            pwd=tournoi_data.get("pwd")
        )
        tournoi.set_id(tournoi_data.get("_id"))
        tournois_list.append(tournoi)

    return tournois_list
    
def supprimer_tournoi(nom_tournoi, pwd):
    tournoi = rechercher_tournoi(nom_tournoi)

    if tournoi:
        if tournoi.get_pwd() == pwd:
            Client2Mongo.collection_tournois().delete_one({"nom": nom_tournoi})
            return tournoi   
        else:
            raise ValueError("Mot de passe incorrect pour supprimer le tournoi")
    else:
        raise ValueError("Aucun tournoi trouvé")

def desinscrire_joueur(tournoi_id, pseudo_joueur):
    # Rechercher le tournoi avec l'identifiant tournoi_id dans la collection tournois
    tournoi = Client2Mongo.collection_tournois().find_one({"_id": tournoi_id})
    if tournoi is None:
        raise ValueError("Tournoi non trouvé")
    
    joueur = Client2Mongo.collection_joueurs().find_one({"pseudo": pseudo_joueur})

    # Vérifier si le joueur est inscrit dans le tournoi
    if joueur["_id"] not in tournoi['list_joueur_dto']:
        raise ValueError("Le joueur n'est pas inscrit dans ce tournoi")

    # Supprimer le joueur de la liste des joueurs du tournoi
    tournoi['list_joueur_dto'].remove(joueur["_id"])

    # Mettre à jour le tournoi dans la collection tournois
    Client2Mongo.collection_tournois().update_one({"_id": tournoi_id}, {"$set": {"list_joueur_dto": tournoi['list_joueur_dto']}})

    return rechercher_tournoi_id(tournoi_id)

def ajout_match(nom_tournoi,match_id):
    # Rechercher le tournoi avec le nom donné
    tournoi_existant = Client2Mongo.collection_tournois().find_one({"nom": nom_tournoi})

    if tournoi_existant: 
        # Rechercher le match avec l'id donné
        match_existant = Client2Mongo.collection_matchs().find_one({"_id": match_id})   

        # Vérifier si l'ID du match est déjà dans la liste des matches du tournoi
        if match_id in tournoi_existant.get("list_match", []):
            raise ValueError("Ce match est déjà inscrit dans ce tournoi.")
        
        if match_existant:
            # Ajouter le joueur à la liste des joueurs du tournoi
            match_tournoi = tournoi_existant.get("list_match", [])
            match_tournoi.append(match_id)
            
            # Mettre à jour le document du tournoi dans la base de données
            Client2Mongo.collection_tournois().update_one({"_id": tournoi_existant["_id"]}, {"$set": {"list_match": match_tournoi}})
            print("Joueur ajouté au tournoi.")
        else:
            raise ValueError("Le match n'existe pas") 
    else:
        raise ValueError("Le tournoi n'existe pas") 

def recuperer_joueurs(nom_tournoi):
    tournoi = Client2Mongo.collection_tournois().find_one({"nom":nom_tournoi})

    if tournoi:
        # Récupérer la liste des participants du tournoi
        participants = []
        joueur = tournoi.get("list_joueur_dto", [])
        #return joueur_id
        for joueurs_list in joueur:
            joueur_id = joueurs_list["_id"]
            participants.append(joueur_id)  # Ou tout autre attribut du joueur que vous souhaitez utiliser

        if participants:
            return participants
        else:
            raise ValueError("Aucun participant trouvé pour ce tournoi.")

    else:
        raise ValueError("Tournoi non trouvé.")    


