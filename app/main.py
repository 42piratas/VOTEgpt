from flask import Flask, jsonify, render_template
from chatgpt.requests import get_candidate_by_country_and_election, get_country_elections, verify_democratic
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
    return render_template("index.html", countries=countries)

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
    candidate = {
        "id": 1,
        "name": "John Doe",
        "known_as": "JD",
        "born": "1965-05-15",
        "nationality": "American",
        "religion": "Christian",
        "education": "Harvard University, BA in Political Science",
        "bio": "John Doe is a seasoned politician with over 30 years of experience in public service...",
        "current_party": "Democratic Party",
        "previous_parties": ["Independent", "Republican"],
        "platform": "Focused on healthcare reform, economic equality, and climate change.",
        "keywords": ["healthcare", "economy", "climate"],
        "political_experience": "Served as a senator for 20 years, mayor for 8 years.",
        "notorious_for": "Advocating for universal healthcare.",
        "endorsements": ["Healthcare Workers Union", "Environmental Protection Group"],
        "funding_sources": ["Small Donations", "Environmental NGOs"],
        "criminal_records": [],
        "abortion": "Pro-choice, supports access to safe and legal abortions.",
        "health_care": "Advocates for universal healthcare.",
        "economy": "Supports progressive taxation and economic equality.",
        "immigration": "Favors comprehensive immigration reform with a path to citizenship.",
        "gun_control": "Supports strict background checks and restrictions on assault weapons.",
        "gun_control_short": "Pro-gun control.",
        "climate_change": "Supports aggressive measures to combat climate change.",
        "taxes": "Supports higher taxes on the wealthy.",
        "lgbtq_rights": "Strong advocate for LGBTQ+ rights, supports marriage equality.",
        "lgbtq_rights_short": "Pro-LGBTQ+ rights.",
        "foreign_policy": "Favors diplomatic solutions and international cooperation.",
        "drug_policy": "Supports decriminalization of marijuana.",
        "criminal_justice_reform": "Advocates for reforming the criminal justice system to reduce incarceration rates.",
        "military_spending": "Favors reducing military spending in favor of domestic programs.",
        "voting_rights": "Supports expanding voting rights and making voting more accessible."
    }

    return render_template("candidate.html", candidate=candidate)

if __name__ == "__main__":
    app.run(debug=True)
