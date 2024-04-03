from flask import Blueprint, request, jsonify
import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
import Service.service_joueur as service_joueur

joueur_bp = Blueprint('joueur_bp', __name__)

@joueur_bp.route('/afficher/<string:pseudo>/', methods=['GET'])
def trouver_un_joueur(pseudo):
    joueur = service_joueur.rechercher_joueur(pseudo)
    if joueur:
        return jsonify(joueur.__dict__)
    else:
        return jsonify({"message": "Joueur non trouvé"})
    
@joueur_bp.route('/ajouter/', methods=['POST'])
def creer_un_joueur():
    data = request.json
    return jsonify(service_joueur.creer_joueur(data.get("nom"),data.get("prenom"),data.get("pseudo"),data.get("age"),data.get("niveau"),data.get("mail")
    ).__dict__)

@joueur_bp.route('/supprimer/', methods=['DELETE'])
def supprimer_un_joueur():
    data = request.get_json() 
    pseudo = data['pseudo']
    return jsonify(service_joueur.supprimer_joueur(pseudo).__dict__)


@joueur_bp.route('/afficher/list/', methods=['GET'])
def list_joueurs():
    joueurs = service_joueur.get_joueurs()
    return jsonify([joueur.__dict__ for joueur in joueurs])

@joueur_bp.route('/modifier/<string:pseudo>/', methods=['PUT'])
def modifier_un_joueur(pseudo):
    data = request.get_json()
    nouveau_nom = data['nom'] 
    nouveau_prenom = data['prenom']
    nouveau_pseudo = data.get("pseudo")
    nouveau_age = data.get("age")
    nouveau_niveau = data.get("niveau")
    nouveau_mail = data.get("mail")
    return jsonify(service_joueur.modifier_joueur(pseudo, nouveau_nom, nouveau_prenom, nouveau_pseudo, nouveau_age, nouveau_niveau, nouveau_mail).__dict__)
    

    