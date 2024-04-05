import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
from client_mongo import Client2Mongo

class TournoiDTO:

    def __init__(self, nom, date, duree, lieu, list_joueur_dto, list_match, pwd):
        self._id = Client2Mongo.id_tournoi()
        self.nom = nom
        self.date = date
        self.duree = duree
        self.lieu = lieu
        self.list_joueur_dto = list_joueur_dto
        self.list_match = list_match
        self.pwd = pwd
    
    def get_id(self):
        return self._id
    
    def set_id(self, value):
        self._id = value
    
    def get_nom(self):
        return self.nom
    
    def set_nom(self, value):
        self.nom = value
    
    def get_date(self):
        return self.date
    
    def set_date(self, value):
        self.date = value
    
    def get_duree(self):
        return self.duree
    
    def set_duree(self, value):
        self.duree = value
    
    def get_lieu(self):
        return self.lieu
    
    def set_lieu(self, value):
        self.lieu = value
    
    def get_list_joueur_dto(self):
        return self.list_joueur_dto
    
    def set_list_joueur_dto(self, value):
        self.list_joueur_dto = value
    
    def get_list_match(self):
        return self.list_match
    
    def set_list_match(self, value):
        self.list_match = value
    
    def get_pwd(self):
        return self.pwd
    
    def set_pwd(self, value):
        self.pwd = value

    def add_joueur(self, joueur):
        if self.list_joueur_dto is None:
            self.list_joueur_dto = []
        self.list_joueur_dto.append(joueur)
        
    def add_match(self, match):
        self.list_match.append(match)