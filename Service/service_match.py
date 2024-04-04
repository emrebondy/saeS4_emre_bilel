import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
from client_mongo import Client2Mongo
from DTO.match_dto import MatchDTO
from Service.service_joueur import rechercher_joueur, rechercher_joueur_par_id

def inserer_match(joueur1_pseudo, joueur2_pseudo, gagnant_pseudo, score1, score2):

    joueur1 = rechercher_joueur(joueur1_pseudo)
    joueur2 = rechercher_joueur(joueur2_pseudo)
    gagnant = rechercher_joueur(gagnant_pseudo)
    
    if condition_match(joueur1.get_id(),joueur2.get_id(),gagnant.get_id(),score1,score2):
        
        match = MatchDTO(participants=[joueur1.get_id(), joueur2.get_id()], gagnant=gagnant.get_id(), scores=[score1,score2])
        # Insertion du match dans la base de données
        Client2Mongo.collection_matchs().insert_one(match.__dict__)

        return match

def inserer_match_sans_score(joueur1_pseudo, joueur2_pseudo):

    joueur1 = rechercher_joueur(joueur1_pseudo)
    joueur2 = rechercher_joueur(joueur2_pseudo)

    if joueur1 and joueur2:

        match = MatchDTO(participants=[joueur1.get_id(), joueur2.get_id()])
        # Insertion du match dans la base de données
        Client2Mongo.collection_matchs().insert_one(match.__dict)

        return match

def condition_match(joueur1, joueur2, gagnant, score1, score2):
    # Vérification des scores
    if score1 < 0 or score2 < 0:
        raise ValueError("Les scores ne doivent pas être négatifs")

    # Vérification des scores ne dépassent pas 11
    if score1 > 11 or score2 > 11:
        raise ValueError("Au ping-pong le score ne doit pas dépasser 11")
    
    # Vérification qu'un joueur à 11 point
    if not (score1 == 11 or score2 == 11):
        raise ValueError("Aucun joueur à 11 point donc personne à gagner")
    
    # Vérification que le gagnant fait partie d'un des deux joueurs
    if gagnant not in (joueur1, joueur2):
        raise ValueError("Le gagnant doit être l'un des joueurs passés en paramètre")
    
    # Vérification de deux joueur différent
    if joueur1 == joueur2:
        raise ValueError("Un joueur ne peut pas jouer contre lui même :-)")

    # Vérification des joueurs
    if not joueur1:
        raise ValueError(f"Le joueur:{joueur1} n existe pas")
    if not joueur2:
        raise ValueError(f"Le joueur:{joueur2} n existe pas")

    # Vérification des types 
    if not all(isinstance(x, int) for x in [joueur1, joueur2, gagnant, score1, score2]):
        raise ValueError("Tous les paramètres doivent être des entiers")
    
    # Vérification du score
    if score1 == score2:
        raise ValueError("Les scores des joueurs sont égaux, impossible de déterminer un gagnant")
    elif gagnant == joueur1 and score1 < score2:
        raise ValueError(f"Le joueur {joueur1} ne peut pas être déclaré gagnant avec un score inférieur à celui du joueur {joueur2}")
    elif gagnant == joueur2 and score2 < score1:
        raise ValueError(f"Le joueur {joueur2} ne peut pas être déclaré gagnant avec un score inférieur à celui du joueur {joueur1}")    
    
    return True

def rechercher_match(_id):
    match_data = Client2Mongo.collection_matchs().find_one({"_id": _id})
    if match_data:
        participants_ids = match_data.get("participants", [])
        participants = []
        for joueur_id in participants_ids:
            joueur_dto = rechercher_joueur_par_id(joueur_id)
            if joueur_dto:
                participants.append(joueur_dto.get_id())
        
        scores = match_data.get("scores", [])
        gagnant_id = match_data.get("gagnant")
        
        match_dto = MatchDTO(
            participants=participants,
            scores=scores,
            gagnant=gagnant_id
        )
        match_dto.set_id(match_data.get("_id"))
        return match_dto
    else:
        return None
    
def supprimer_match(_id):
    match = rechercher_match(_id) 
    Client2Mongo.collection_matchs().delete_one({"_id": match.get_id()})
    return match
    
def lister_tous_les_matchs():
    matchs_data = Client2Mongo.collection_matchs().find()
    liste_matchs = []
    for match_data in matchs_data:
        participants_ids = match_data.get("participants", [])
        participants = []
        for joueur_id in participants_ids:
            joueur_dto = rechercher_joueur_par_id(joueur_id)
            if joueur_dto:
                participants.append(joueur_dto.get_id())
        
        scores = match_data.get("scores", [])
        gagnant_id = match_data.get("gagnant")
        
        match_dto = MatchDTO(
            participants=participants,
            scores=scores,
            gagnant=gagnant_id
        )
        match_dto.set_id(match_data.get("_id"))
        liste_matchs.append(match_dto)
    return liste_matchs