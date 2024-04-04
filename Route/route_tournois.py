from flask import Blueprint, request, jsonify
import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
import Service.service_tournoi as service_tournoi

tournoi_bp = Blueprint('tournoi_bp', __name__)         

@tournoi_bp.route('/afficher/<string:nom>/', methods=['GET'])
def rechercher_un_tournoi(nom):
    tournoi = service_tournoi.rechercher_tournoi(nom)
    if tournoi:
        return jsonify(tournoi.__dict__)
    else:
        return jsonify({"message": "Tournoi non trouvé"})

@tournoi_bp.route('/afficher/<int:_id>/', methods=['GET'])
def rechercher_un_tournoi2(_id):
    tournoi = service_tournoi.rechercher_tournoi_id(_id)
    if tournoi:
        return jsonify(tournoi.__dict__)
    else:
        return jsonify({"message": "Tournoi non trouvé"}) 
    
@tournoi_bp.route('/ajouter/', methods=['POST'])
def creer_un_tournoi():
    data = request.json  
    return jsonify(service_tournoi.creer_tournoi(data.get("nom"), data.get("date"), data.get("duree"), data.get("lieu"), data.get("pwd")).__dict__)   

@tournoi_bp.route('/inscrire/', methods=['PUT'])
def ajouter_joueur_tournoi():
    data = request.json
    id_tournoi = data.get("_id")
    pseudo = data.get("pseudo")
    return jsonify(service_tournoi.inscrire_joueur_au_tournoi(pseudo, id_tournoi).__dict__)
    
    
@tournoi_bp.route('/afficher/list/', methods=['GET'])
def rechercher_list_tournoi():
    tournois = service_tournoi.get_tournois()
    return jsonify([tournoi.__dict__ for tournoi in tournois])



@tournoi_bp.route('/supprimer/', methods=['DELETE'])
def supprimer_un_tournoi():
    data = request.json
    nom_tournoi = data.get("nom_tournoi")
    pwd = data.get("pwd")
    return jsonify(service_tournoi.supprimer_tournoi(nom_tournoi, pwd).__dict__)

# désinscription d'un tournoi
@tournoi_bp.route('/desinscription/', methods=['PUT'])
def desinscrire_un_joueur():
    data = request.json
    tournoi_id = data.get("tournoi_id")
    pseudo_joueur = data.get("pseudo_joueur")
    service_tournoi.desinscrire_joueur(tournoi_id, pseudo_joueur)
    return jsonify({"message": "joueur desinscrit"})

#ajouter un match dans tournoi
@tournoi_bp.route('/ajouter_match/', methods=['PUT'])
def ajouter_match_tournoi():
    data = request.json
    nom_tournoi = data.get("nom_tournoi")
    match_id = data.get("match_id")
    service_tournoi.ajout_match(nom_tournoi,match_id)
    return jsonify({"message": "match ajouter"})

# lancer le tournoi et organiser les match 
@tournoi_bp.route('/lancer_tournoi/', methods=['POST'])
def lancer_tournoi():
    data = request.json
    nom_tournoi = data.get("nom_tournoi")
    return service_tournoi.recuperer_joueurs(nom_tournoi)