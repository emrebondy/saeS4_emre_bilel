import sys
sys.path.append('/home/bilel/prive/saeAngularPython/tournoiPingPong')
from client_mongo import Client2Mongo

class JoueurDTO:
    
    nombre_instance = Client2Mongo.compter_nombre_joueur()

    def __init__(self, nom, prenom, pseudo, age, niveau, email):
        self._id = JoueurDTO.nombre_instance + 1
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.age = age
        self.niveau = niveau
        self.email = email
        JoueurDTO.nombre_instance += 1
    
    def get_id(self):
        return self._id
    
    def set_id(self, value):
        self._id = value
        
    def get_nom(self):
        return self.nom
    
    def set_nom(self, value):
        self.nom = value
    
    def get_prenom(self):
        return self.prenom
    
    def set_prenom(self, value):
        self.prenom = value
    
    def get_pseudo(self):
        return self.pseudo
    
    def set_pseudo(self, value):
        self.pseudo = value
    
    def get_age(self):
        return self.age
    
    def set_age(self, value):
        self.age = value
    
    def get_niveau(self):
        return self.niveau
    
    def set_niveau(self, value):
        self.niveau = value
    
    def get_email(self):
        return self.email
    
    def set_email(self, value):
        self.email = value

if __name__ == "__main__":
    pass
