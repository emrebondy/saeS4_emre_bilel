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
    tournoi = rechercher_tournoi_id(_id)
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

if __name__ == "__main__":
    print(supprimer_tournoi("Tournoi", "mdp"))