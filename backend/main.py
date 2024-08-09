from flask import Flask, render_template
from chatgpt.requests import get_country_elections, verify_democratic
from database.db_setup import db
from config import Config
from flask_migrate import Migrate
from functions import get_countries

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
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
    return verify_democratic(country)

@app.route("/elections/<string:country>/<string:country_id>/")
def getElections(country, country_id):
    return get_country_elections(country, country_id)

@app.route("/election/<string:election_id>/")
def getElection(election_id):
    return election_id

@app.route("/candidate/<string:candidate_id>/")
def getCandidate(candidate_id):
    return candidate_id

if __name__ == "__main__":
    app.run(debug=True)
