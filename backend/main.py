from flask import Flask, jsonify, render_template
from chatgpt.requests import get_country_elections, verify_democratic
from database.db_setup import db
from decouple import config
from flask_migrate import Migrate
from functions import get_countries, get_elections_by_id

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
@app.route("/index")
def index():
    countries = get_countries()
    return render_template("index.html", countries=countries)

@app.route("/democracy/<string:country>/")
def getDemocracy(country):
    result = verify_democratic(country)
    return jsonify(result)

@app.route("/elections/<string:country>/<string:country_id>/")
def getElections(country, country_id):
    try:
        # Converta o country_id de string para inteiro
        country_id = int(country_id)
    except ValueError:
        return jsonify({"error": "Invalid country_id, expected an integer."}), 400

    result = get_country_elections(country, country_id)
    return jsonify(result)

@app.route("/election/<string:election_id>/")
def getElection(election_id):
    # Aqui você pode retornar dados de uma eleição específica, possivelmente buscando do banco de dados
    election = get_elections_by_id(election_id)
    # return election
    return render_template("election.html", election=election)

@app.route("/candidate/<string:candidate_id>/")
def getCandidate(candidate_id):
    # Aqui você pode retornar dados de um candidato específico, possivelmente buscando do banco de dados
    return jsonify({"candidate_id": candidate_id})

if __name__ == "__main__":
    app.run(debug=True)
