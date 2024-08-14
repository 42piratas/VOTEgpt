from database.db_setup import db
from database.models import Candidate, Country, ElectionData

def get_countries():
    try:
        # Fetch all countries from the database
        countries = Country.query.all()
        
        # Serialize data to JSON
        countries_list = [
            {
                'id': country.id,
                'label': country.label,
                'code': country.code,
                'is_democracy': country.is_democracy
            } for country in countries
        ]
        # Return the list of countries
        return countries_list
    except Exception as e:
        print(f"Error fetching countries: {e}")
        return []
    
def insert_election(election_type, election_date, country_id):
    """
    Inserts a new election data entry into the ElectionData table.
    
    :param type_election: Type of elecion (e.g., presidential, state)
    :param election_date: Election date (object datetime.date)
    :param country_id: ID of the country to which the election data refers
    :return: The new ElectionData object if successful, None otherwise
    """
    try:
        new_election = ElectionData(election_type=election_type, election_date=election_date, country_id=country_id)
        db.session.add(new_election)
        db.session.commit()
        print(f"Election {election_type} added successfully.")
        return new_election
    except Exception as e:
        print(f"Error adding election {election_type}: {e}")
        db.session.rollback()
        return None
    
def get_elections_by_id(election_id):
    try:
        # Fetch election data by ID
        election = ElectionData.query.filter_by(id=election_id).first()
        country = Country.query.filter_by(id=election.country_id).first()
        # candidate = Candidate.query.filter_by(id=election.candidate_id).first()
        
        
        # Serialize data to JSON
        election_data = {
            'id': election.id,
            'election_type': election.election_type,
            'election_date': election.election_date,
            'country': {
                            'id': country.id,
                            'label': country.label,
                            'code': country.code,
                        },
            "candidate": {
                            'id': 1,
                            'name': 'Donand John Trump',
                            'known_as': 'Donand Trump',
                            'url_image': 'images/candidates/Donald_Trump_official_portrait.jpg',
                            'current_party': 'Republican',
                            'platform': 'tax cuts and deregulation, border wall and strict immigration policies, renegotiating trade deals, repeal and replace Obamacare, “America First” foreign policy.',
                            'keywords': 'Impeachment, Real Estate, Election Controversy, Immigration, Trade Policies',
                        },
            'sources': election.sources,
        }
        
        # Return the election data
        return election_data
    except Exception as e:
        print(f"Error fetching election {election_id}: {e}")
        return {}
    