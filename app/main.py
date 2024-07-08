from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return "VOTEGPT Index Page"

@app.route("/election/<string:election_id>/")
def getElection(election_id):
    return election_id

@app.route("/candidate/<string:candidate_id>/")
def getCandidate(candidate_id):
    return candidate_id

if __name__ == "__main__":
    app.run(debug=True)
