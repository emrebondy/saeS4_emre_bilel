from flask import Blueprint, request, jsonify
import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
import Service.service_match as service_match

match_bp = Blueprint('match_bp', __name__)


#afficher tout les matchs
@match_bp.route('/', methods=['GET'])
def afficher_liste_matchs():
    matchs = service_match.lister_tous_les_matchs()
    return jsonify([match.__dict__ for match in matchs])


#afficher un match par id
@match_bp.route('/<int:_id>/', methods=['GET'])
def rechercher_un_match(_id):
    match = service_match.rechercher_match(_id)
    if match:
        return jsonify(match.__dict__)
    else:
        return jsonify({"message": "match non trouvé"})    
    

#ajouter un match
@match_bp.route('/', methods=['POST'])
def creer_un_match_sans_score():
    data = request.json  
    joueur1 = data.get("joueur1")  
    joueur2 = data.get("joueur2")
    return jsonify(service_match.inserer_match_sans_score(joueur1, joueur2).__dict__)

          

#supprimer un match
@match_bp.route('/', methods=['DELETE'])
def supprimer_un_match():
    data = request.get_json() 
    _id = data['_id']
    return jsonify(service_match.supprimer_match(_id).__dict__)


    