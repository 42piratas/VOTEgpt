from chatgpt.requests import get_candidate_by_country_and_election
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
        # Querying election and related country data
        election = db.session.query(ElectionData).join(Country).filter(ElectionData.id == election_id).first()
        candidate = get_candidate_by_country_and_election(election)
        print(candidate)
        if not candidate:
            election_data = {
                'id': election.id,
                'election_type': election.election_type,
                'election_date': election.election_date,
                'country': {
                                'id': election.country_id,
                                'label': election.country.label,
                                'code': election.country.code,
                            },
                'sources': election.sources,
            }
            
            # Return the election data
            return election_data
        # candidate = Candidate.query.filter_by(election_id=election.id).first()
        # print(candidate)
    
        # Serialize data to JSON
        election_data = {
            'id': election.id,
            'election_type': election.election_type,
            'election_date': election.election_date,
            'country': {
                            'id': election.country_id,
                            'label': election.country.label,
                            'code': election.country.code,
                        },
            'candidate': candidate,
            # 'candidate': [{
            #     "id": 1,
            #     "name": "John Doe",
            #     "known_as": "JD",
            #     "born": "1965-05-15",
            #     "nationality": "American",
            #     "religion": "Christian",
            #     "education": "Harvard University, BA in Political Science",
            #     "bio": "John Doe is a seasoned politician with over 30 years of experience in public service...",
            #     "current_party": "Democratic Party",
            #     "previous_parties": ["Independent", "Republican"],
            #     "platform": "Focused on healthcare reform, economic equality, and climate change.",
            #     "keywords": ["healthcare", "economy", "climate"],
            #     "political_experience": "Served as a senator for 20 years, mayor for 8 years.",
            #     "notorious_for": "Advocating for universal healthcare.",
            #     "endorsements": ["Healthcare Workers Union", "Environmental Protection Group"],
            #     "funding_sources": ["Small Donations", "Environmental NGOs"],
            #     "criminal_records": [],
            #     "abortion": "Pro-choice, supports access to safe and legal abortions.",
            #     "health_care": "Advocates for universal healthcare.",
            #     "economy": "Supports progressive taxation and economic equality.",
            #     "immigration": "Favors comprehensive immigration reform with a path to citizenship.",
            #     "gun_control": "Supports strict background checks and restrictions on assault weapons.",
            #     "gun_control_short": "Pro-gun control.",
            #     "climate_change": "Supports aggressive measures to combat climate change.",
            #     "taxes": "Supports higher taxes on the wealthy.",
            #     "lgbtq_rights": "Strong advocate for LGBTQ+ rights, supports marriage equality.",
            #     "lgbtq_rights_short": "Pro-LGBTQ+ rights.",
            #     "foreign_policy": "Favors diplomatic solutions and international cooperation.",
            #     "drug_policy": "Supports decriminalization of marijuana.",
            #     "criminal_justice_reform": "Advocates for reforming the criminal justice system to reduce incarceration rates.",
            #     "military_spending": "Favors reducing military spending in favor of domestic programs.",
            #     "voting_rights": "Supports expanding voting rights and making voting more accessible."
            # }],
            'sources': election.sources,
        }
        # Return the election data
        return election_data
    except Exception as e:
        print(f"Error fetching election {election_id}: {e}")
        return {}
    
def get_candidate_by_id(candidate_id):
    try:
        # Fetch candidate data by ID
        candidate = Candidate.query.get(candidate_id)
        
        # Serialize data to JSON
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
            for candidate in candidate
        ]
        return {
            "candidates": True,
            "data": candidates_data,
            "sources": candidates_data[0]["sources"] if candidates_data else []
        }
    except Exception as e:
        print(f"Error fetching candidate {candidate_id}: {e}")
        return {"candidates": False, "data": [], "sources": []}
