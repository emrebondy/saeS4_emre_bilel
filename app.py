from flask import Flask
from Route.route_joueurs import joueur_bp

app = Flask(__name__)

app.register_blueprint(joueur_bp, url_prefix='/joueurs')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()