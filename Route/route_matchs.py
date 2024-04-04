from flask import Blueprint, request, jsonify
import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
import Service.service_match as service_match

match_bp = Blueprint('match_bp', __name__)


#ajouter un match
@match_bp.route('/ajouter/', methods=['POST'])
def creer_un_match():
    data = request.json  
    joueur1 = data.get("joueur1")  
    joueur2 = data.get("joueur2")
    gagnant = data.get("gagnant")
    score1 = data.get("score1")
    score2 = data.get("score2")
    return jsonify(service_match.inserer_match(joueur1, joueur2, gagnant, score1, score2).__dict__)

#ajouter un match
@match_bp.route('/ajoute/', methods=['POST'])
def creer_un_match_sans_score():
    data = request.json  
    joueur1 = data.get("joueur1")  
    joueur2 = data.get("joueur2")
    return jsonify(service_match.inserer_match_sans_score(joueur1, joueur2).__dict__)

#afficher un match par id
@match_bp.route('/afficher/<int:_id>/', methods=['GET'])
def rechercher_un_match(_id):
    match = service_match.rechercher_match(_id)
    if match:
        return jsonify(match.__dict__)
    else:
        return jsonify({"message": "match non trouvé"})              

#supprimer un match
@match_bp.route('/supprimer/', methods=['DELETE'])
def supprimer_un_match():
    data = request.get_json() 
    _id = data['_id']
    return jsonify(service_match.supprimer_match(_id).__dict__)

@match_bp.route('/afficher/list/', methods=['GET'])
def afficher_liste_matchs():
    matchs = service_match.lister_tous_les_matchs()
    return jsonify([match.__dict__ for match in matchs])

    