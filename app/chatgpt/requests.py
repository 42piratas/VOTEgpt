import ast
import json
import re
from decouple import config
from flask import jsonify
from openai import OpenAI
from database.models import Candidate, Country, ElectionData
from database.db_setup import db

client = OpenAI(
    api_key=config('OPENAI_API_KEY'),
)

sources_strict = "Refer only to the following sources: International Foundation for Electoral Systems (IFES), ElectionGuide.org, Inter-Parliamentary Union (IPU), and International IDEA."

sources_reliable = "Ensure the data is sourced from reliable, impartial sources, such as academic publications, official electoral bodies, government reports, reputable non-partisan organizations, International Foundation for Electoral Systems (IFES), ElectionGuide.org, Inter-Parliamentary Union (IPU), and International IDEA."

# This query has already been performed and adjusted in the database.
# It is still here because it can be used in the future.
def verify_democratic(country_id):
    country = Country.query.filter_by(id=country_id).first()
    if not country:
        return jsonify({"error": "Country not found."}), 404
    if country.is_democracy:
        return True
    else:
        return False

def get_country_elections(country, country_id):
    try:
        # Make sure country_id is an integer
        if not isinstance(country_id, int):
            raise ValueError("Invalid country_id, expected an integer.")
        
        # check if country is democratic or not
        democratic = verify_democratic(country_id)
        if not democratic:
            print(f"{country} is not a democratic country.")
            return {
                "elections": "Non-democratic",
                "data": f"{country} is not a democratic country.",
                "sources": []
            }

        # Check if there are already elections in the database for the country within the desired period
        existing_elections = ElectionData.query.filter_by(country_id=country_id).all()

        if existing_elections:
            # If there are elections in the database, return that data with the sources
            elections_data = [
                {
                    "id": election.id,
                    "election_type": election.election_type,
                    "date": election.election_date,
                    "sources": election.sources.split(",") if election.sources else []
                }
                for election in existing_elections
            ]
            return {
                "elections": True,
                "data": elections_data,
                "sources": elections_data[0]["sources"] if elections_data else []
            }

        # If there is no data, perform a query on ChatGPT
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f'Please, check if {country} has presidential elections schedule for any time in the next 6 months, given todays date. '
                        'If there are, list the types of elections, the scheduled dates for these elections, and provide the sources of this information. '
                        'Format the response as follows: '
                        '[[{"election_type": "Type of Election 1","date": "Date 1"}, ...], ["Source 1s URL", ..., "Source Ns URL"]]. '
                        f'If there ar no elections schedule to {country}, return only "FALSE" and the sources, formatted as '
                        f'[FALSE, ["Source 1"s URL", ..., "Source N"s URL"]] {sources_strict}'
                    ),
                },
            ],
        )
        data = completion.choices[0].message.content
        # if model has FALSE return message of no upcomming elections and source
        if 'FALSE' in data:
            return {
                "elections": False,
                "sources": ['https://www.ifes.org', 'https://www.electionguide.org', 'https://www.ipu.org', 'https://www.idea.int']
            }
        #Replacing 'FALSE' with 'False' to be recognized as boolean in Python
        # string = data.replace('FALSE', 'False')

        # Turning the string into an array
        # array = ast.literal_eval(string)
        data = ast.literal_eval(data)
        # data=json.loads(array)

        elections = data[0]
        sources = data[1]

        # If there are elections, enter them into the database
        inserted_elections = []
        for election in elections:
            inserted = insert_election(
                election['election_type'],
                election['date'],
                country_id,
                sources=",".join(sources)  # Add sources when inserting the election
            )
            if inserted:
                inserted_elections.append({
                    'election_type': election['election_type'],
                    'date': election['date']
                })

        return {"elections": True, "data": inserted_elections, "sources": sources}

    except ValueError as ve:
        print(f"Error (ValueError): {ve}")
        return {"error": str(ve)}
    except Exception as e:
        print(f"Error fetching elections (Exception): {e}")
        return {"error": f"An error occurred while fetching elections: {e}"}

def insert_election(election_type, election_date, country_id, sources):
    try:
        # Check if country exists using ID (country_id)
        country = db.session.query(Country).filter_by(id=country_id).first()
        if not country:
            return jsonify({"error": "Country not found."}), 404

        new_election = ElectionData(
            election_type=election_type,
            election_date=election_date,
            country_id=country.id,
            sources=sources
        )
        db.session.add(new_election)
        db.session.commit()
        print(f"Election {election_type} on {election_date} added successfully.")
        return new_election
    except Exception as e:
        print(f"Error adding election {election_type} on {election_date}: {e}")
        db.session.rollback()
        return None
    
def get_candidate_by_country_and_election(election):
    try:
        existing_candidates = Candidate.query.filter_by(election_id=election.id).all()
        print('existing_candidates:', existing_candidates)
        if existing_candidates:
            # Se houver candidatos na base de dados, retornamos os dados com as informações relevantes
            candidates_data = [
                {
                    "id": candidate.id,
                    "name": candidate.name,
                    "known_as": candidate.known_as,
                    "born": candidate.born,
                    "nationality": candidate.nationality,
                    "religion": candidate.religion,
                    "education": candidate.education,
                    "bio": candidate.bio,
                    "current_party": candidate.current_party,
                    "previous_parties": candidate.previous_parties.split(",") if candidate.previous_parties else [],
                    "platform": candidate.platform,
                    "keywords": candidate.keywords.split(",") if candidate.keywords else [],
                    "political_experience": candidate.political_experience,
                    "notorious_for": candidate.notorious_for,
                    "endorsements": candidate.endorsements.split(",") if candidate.endorsements else [],
                    "funding_sources": candidate.funding_sources.split(",") if candidate.funding_sources else [],
                    "criminal_records": candidate.criminal_records.split(",") if candidate.criminal_records else [],
                    "abortion": candidate.abortion,
                    "health_care": candidate.health_care,
                    "economy": candidate.economy,
                    "immigration": candidate.immigration,
                    "gun_control": candidate.gun_control,
                    "gun_control_short": candidate.gun_control_short,
                    "climate_change": candidate.climate_change,
                    "taxes": candidate.taxes,
                    "lgbtq_rights": candidate.lgbtq_rights,
                    "lgbtq_rights_short": candidate.lgbtq_rights_short,
                    "foreign_policy": candidate.foreign_policy,
                    "drug_policy": candidate.drug_policy,
                    "criminal_justice_reform": candidate.criminal_justice_reform,
                    "military_spending": candidate.military_spending,
                    "voting_rights": candidate.voting_rights,
                }
                for candidate in existing_candidates
            ]
            return {
                "candidates": True,
                "data": candidates_data,
                "sources": candidates_data[0]["sources"] if candidates_data else []
            }
        content_message = f'Please, provide a list of the full names of all candidates participating in the upcoming {election.election_type} elections in {election.country.label} in {election.election_date}. Format the response as follows: ["{election.country.label}", "{election.election_type}", "{election.election_date}", ["Full Name 1", "Full Name 2", ..., "Full Name N"], ["Source 1s URL", ..., "Source Ns URL"]]. Include only the candidates full names and the sources in the list. If there ar no elections schedule to {election.country.label}, return only "FALSE" and the sources, formatted as [FALSE, ["Source 1s URL", ..., "Source Ns URL"]]. {sources_reliable}'

        # If there is no data, perform a query on ChatGPT
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": content_message,
                },
            ],
        )
        data = completion.choices[0].message.content
        print('return candidate from chatgpt:',data)
        if 'FALSE' in data:
            return {
                "elections": False,
                "sources": ["IFES", "ElectionGuide.org", "IPU", "International IDEA"]
            }
        resultado = ast.literal_eval(data)
        
        return {"elections": True, "data": resultado[0], "sources": resultado[1]}

    except ValueError as ve:
        print(f"Error: {ve}")
        return {"error": str(ve)}
    except Exception as e:
        print(f"Error fetching elections: {e}")
        return {"error": f"An error occurred while fetching elections: {e}"}