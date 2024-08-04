# app.py# main.py
from chatgpt.requests import *
from database.functions import get_countries
from db_setup import db
from models import Country
from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
@app.route('/index')
def index():
    return "VOTEGPT Index Page"

@app.route('/countries', methods=['GET'])
def getCountries():
    return get_countries()

@app.route('/democracy/<country>')
def isDemocraticCountry(country):
    return verify_democratic(country)

@app.route('/elections/<country>')
def getElectionsByCountry(country):
    return get_country_elections(country)

@app.route('/candidates/<country>/<election_type>/<election_date>')
def getCandidatesByCountryAndElection(country, election_type, election_date):
    return get_candidates_by_country_and_election(country, election_type, election_date)

# Importa os módulos que contêm as rotas e os modelos
if __name__ == "__main__":
    app.run(debug=True)