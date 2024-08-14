from flask import Blueprint, render_template, request
from .data import elections_data, candidates_data  # Import the election and candidates data

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_country = request.form.get("country")
        elections = elections_data.get(selected_country, [])
        if elections:
            return render_template("elections.html", country=selected_country, elections=elections)
        else:
            return render_template("no_elections.html", country=selected_country)
    return render_template("index.html", countries=elections_data.keys())

@main.route("/election/<int:election_id>/")
def get_election(election_id):
    candidates = candidates_data.get(str(election_id), [])
    return render_template("election.html", election_id=election_id, candidates=candidates)

@main.route("/candidate/<int:candidate_id>/")
def get_candidate(candidate_id):
    # Find the candidate details from candidates_data
    for election_candidates in candidates_data.values():
        for candidate in election_candidates:
            if candidate['id'] == str(candidate_id):
                return render_template("candidate.html", candidate=candidate)
    return "Candidate not found", 404
