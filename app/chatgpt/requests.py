import json
import re
from decouple import config
from openai import OpenAI
from database.models import Country, ElectionData
from database.db_setup import db

client = OpenAI(
    api_key=config('OPENAI_API_KEY'),
)

sources_strict = "Refer only to the following sources: International Foundation for Electoral Systems (IFES), ElectionGuide.org, Inter-Parliamentary Union (IPU), and International IDEA."

def verify_democratic(country):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": f"Please, respond with only 'TRUE' or 'FALSE': is {country} democratic or not? Format the response as follows: [TRUE|FALSE, ['Source 1's URL', ..., 'Source N's URL']]. {sources_strict}",
            },
        ],
    )
    data = completion.choices[0].message.content
    data = re.sub(r"(?<!\\)'", '"', data)  # Fix apostrophes to double quotes
    data = json.loads(data)  # Convert JSON string to Python object
    
    return {
        "democratic": data[0],
        "sources": data[1]
    }

def get_country_elections(country, country_id):
    try:
        # Make sure country_id is an integer
        if not isinstance(country_id, int):
            raise ValueError("Invalid country_id, expected an integer.")

        # Check if there are already elections in the database for the country within the desired period
        existing_elections = ElectionData.query.filter_by(country_id=country_id).all()

        if existing_elections:
            # Se existirem eleições no banco de dados, retornar esses dados com as fontes
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
        
        content = (
            f"Please, check if {country} has presidential elections schedule for any time in the next 6 months, given today's date. "
            "If there are, list the types of elections, the scheduled dates for these elections, and provide the sources of this information. "
            "Format the response as follows: "
            "[[{'election_type': 'Type of Election 1','date': 'Date 1'}, ...], ['Source 1's URL', ..., 'Source N's URL']]. "
            f"If there ar no elections schedule to {country}, return only 'FALSE' and the sources, formatted as "
            f"[FALSE, ['Source 1's URL', ..., 'Source N's URL']] {sources_strict}"
        )
                    
        
        print(content)

        # If there is no data, perform a query on ChatGPT
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"Please, check if {country} has presidential elections schedule for any time in the next 6 months, given today's date. "
                        "If there are, list the types of elections, the scheduled dates for these elections, and provide the sources of this information. "
                        "Format the response as follows: "
                        "[[{'election_type': 'Type of Election 1','date': 'Date 1'}, ...], ['Source 1's URL', ..., 'Source N's URL']]. "
                        f"If there ar no elections schedule to {country}, return only 'FALSE' and the sources, formatted as "
                        f"[FALSE, ['Source 1's URL', ..., 'Source N's URL']] {sources_strict}"
                    ),
                },
            ],
        )
        data = completion.choices[0].message.content
        # se retorno for neste modelo -> [FALSE, ['https://www.ifes.org', 'https://www.electionguide.org', 'https://www.ipu.org', 'https://www.idea.int']], retornar mensagem de No upcoming elections e as fontes consultadas
        if data == "[FALSE, ['https://www.ifes.org', 'https://www.electionguide.org', 'https://www.ipu.org', 'https://www.idea.int']]":
            return {"elections": False, "sources": ["IFES", "ElectionGuide.org", "IPU", "International IDEA"]}
        data =json.loads(data)
        print("fez consulta no gpto", data)
        # data = re.sub(r"(?<!\\)'", '"', data)  # Fix apostrophes to double quotes
        # data = json.loads(data)  # Convert JSON string to Python object

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
        print(f"Error: {ve}")
        return {"error": str(ve)}
    except Exception as e:
        print(f"Error fetching elections: {e}")
        return {"error": "An error occurred while fetching elections"}

def insert_election(election_type, election_date, country_id, sources):
    try:
        # Check if country exists using ID (country_id)
        country = db.session.query(Country).filter_by(id=country_id).first()
        if not country:
            print(f"Country with id {country_id} not found.")
            return None

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