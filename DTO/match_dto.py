import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
from client_mongo import Client2Mongo

class MatchDTO:

    def __init__(self, participants):
        self._id = Client2Mongo.id_match()
        self.participants = participants

    def get_id(self):
        return self._id

    def get_participants(self):
        return self.participants

    def set_id(self, match_id):
        self._id = match_id

    def set_participants(self, participants):
        self.participants = participants

    def add_participant(self, participant):
        self.participants.append(participant)

