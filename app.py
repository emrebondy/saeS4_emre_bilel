from flask import Flask
from flask_cors import CORS
from Route.route_joueurs import joueur_bp
from Route.route_tournois import tournoi_bp
from Route.route_matchs import match_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(joueur_bp, url_prefix='/joueurs')
app.register_blueprint(tournoi_bp, url_prefix='/tournois')
app.register_blueprint(match_bp, url_prefix='/matchs')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()