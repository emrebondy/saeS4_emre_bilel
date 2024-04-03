from pymongo import MongoClient

class Client2Mongo:

    @staticmethod
    def connexion_mongo():
        client = MongoClient("mongodb://localhost:27017/")
        return client
    
    @staticmethod
    def base_de_donnees():
        database = Client2Mongo.connexion_mongo()["tournoi"]
        return database
    
    @staticmethod
    def collection_joueurs():
        collection_joueur = Client2Mongo.base_de_donnees()["joueurs"]
        return collection_joueur
    
    @staticmethod
    def collection_matchs():
        collection_matchs = Client2Mongo.base_de_donnees()["matchs"]
        return collection_matchs

    @staticmethod
    def collection_tournois():
        collection_tournois = Client2Mongo.base_de_donnees()["tournois"]
        return collection_tournois
    
    @staticmethod
    def compter_nombre_joueur():
        nombre_joueur = Client2Mongo.collection_joueurs().count_documents({})
        return nombre_joueur