from flask import Flask, jsonify, render_template
from chatgpt.requests import get_country_elections, verify_democratic
from database.db_setup import db
from decouple import config
from flask_migrate import Migrate
from functions import get_candidate_by_id, get_countries, get_elections_by_id

app = Flask(__name__)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
@app.route("/index")
def index():
    countries = get_countries()
    wallet_address = config('WALLET_ADDRESS')
    return render_template("index.html", countries=countries, wallet_address=wallet_address)

@app.route("/democracy/<string:country>/")
def getDemocracy(country):
    result = verify_democratic(country)
    return jsonify(result)

@app.route("/elections/<string:country>/<string:country_id>/")
def getElections(country, country_id):
    try:
        country_id = int(country_id)
    except ValueError:
        return jsonify({"error": "Invalid country_id, expected an integer."}), 400

    result = get_country_elections(country, country_id)
    return jsonify(result)

@app.route("/election/<string:election_id>/")
def getElection(election_id):
    election = get_elections_by_id(election_id)
    print(type(election['candidate']))
    return render_template("election.html", election=election, candidates=election['candidate'])

@app.route("/candidate/<string:candidate_id>/")
def getCandidate(candidate_id):
    candidate = get_candidate_by_id(candidate_id)
    return render_template("candidate.html", candidate=candidate)

if __name__ == "__main__":
    app.run(debug=True)