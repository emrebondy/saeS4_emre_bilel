import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
from client_mongo import Client2Mongo

class MatchDTO:

    nombre_instance = Client2Mongo.id_match()
    
    def __init__(self, participants, gagnant, scores):
        self._id = MatchDTO.nombre_instance + 1
        self.participants = participants
        self.gagnant = gagnant
        self.scores = scores
        MatchDTO.nombre_instance += 1

    def get_id(self):
        return self._id

    def get_participants(self):
        return self.participants

    def get_gagnant(self):
        return self.gagnant

    def get_scores(self):
        return self.scores

    def set_id(self, match_id):
        self._id = match_id

    def set_participants(self, participants):
        self.participants = participants

    def set_gagnant(self, gagnant):
        self.gagnant = gagnant

    def set_scores(self, scores):
        self.scores = scores

    def add_participant(self, participant):
        self.participants.append(participant)

    def add_score(self, score):
        self.scores.append(score)