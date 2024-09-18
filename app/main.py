from flask import Flask, jsonify, render_template
from chatgpt.requests import get_country_elections, verify_democratic
from database.db_setup import db
from decouple import config
from flask_migrate import Migrate
from functions import get_candidate_by_id, get_countries, get_elections_by_id
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(
    api_key=config('OPENAI_API_KEY'),
)

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
    wallet_address = config('WALLET_ADDRESS')
    election = get_elections_by_id(election_id)
    #print type of election
    print(election)
    return render_template("election.html", election=election, wallet_address=wallet_address)

# @app.route("/candidate/<string:election_id>")
# def getCandidatesByElction(election_id):
#     # get_candidate_by_country_and_election(election_id)
#     return candidates

# @app.route("/candidate/<string:candidate_id>/")
# def getCandidate(candidate_id):
#     candidate = get_candidate_by_id(candidate_id)
#     return render_template("candidate.html", candidate=candidate)

if __name__ == "__main__":
    app.run(debug=True)