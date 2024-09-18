from chatgpt.requests import get_candidate_by_country_and_election, get_full_data_from_candidate
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
        election = db.session.query(ElectionData).join(Country).filter(ElectionData.id == election_id).first()
        candidate = get_candidate_by_country_and_election(election)
        candidate_full_data = []
        for candidate in candidate['data'][3]:
            candidate_profile_a: str = (
                "Please, provide detailed information about the political candidate "
                "named {candidate_name} from {country}. "
                "Include the following details and return 'Unknown' for any information that is not available. "
                "Format the response as follows: "
                "{{'name': [fullname], 'known_as': [known as],'born': [location, date, age] | 'Unknown', 'nationality': [nationality(ies)] | 'Unknown', "
                "'religion': Religion | 'Unknown', 'education': [education] | 'Unknown', "
                "'current-party': [current-party] | 'Unknown', 'previous-party(ies)': [previous-party(ies)] | 'Unknown', "
                "'abortion': 'Policy on abortion (140 characters max)', "
                "'health-care': 'Policy on health-care (140 characters max)', "
                "'economy': 'Policy on economy (140 characters max)', "
                "'immigration': 'Policy on immigration (140 characters max)', "
                "'gun-control': 'Policy on gun-control (140 characters max)', "
                "'gun-control-short': 'supportive | opposed | neutral | ambiguous | unknown', "
                "'climate-change': 'Policy on climate-change (140 characters max)', "
                "'education-policy': 'Policy on education (140 characters max)', "
                "'taxes': 'Policy on taxes (140 characters max)', "
                "'lgbtq-rights': 'Policy on lgbtq-rights (140 characters max)', "
                "'lgbtq-rights-short': 'supportive | opposed | neutral | ambiguous | unknown', "
                "'foreign-policy': 'Policy on foreign-policy (140 characters max)', "
                "'drug-policy': 'Policy on drug-policy (140 characters max)', "
                "'criminal-justice-reform': 'Policy on criminal-justice-reform (140 characters max)', "
                "'military-spending': 'Policy on military-spending (140 characters max)', "
                "'voting-rights': 'Policy on voting-rights (140 characters max)' "
                "The 'biography' should be limited to 420 characters. "
                "'mini-biography' and 'criminal-records' should be limited to 140 characters. "
                "'platform' and 'notorious-for' should be concise, described only through keywords, straightforward expressions, "
                "and/or very short, objective sentences, with a maximum list of 05 itens for each. "
                "Always avoid redundancies. Format the response as follows: "
                "[{{ 'biography': '<biography> (420 characters max)>' , "
                "'mini-biography': '<mini-biography> (140 characters max)>' , "
                "'platform': ['', '', ... (05 itens max)] , "
                "'criminal-records': '<criminal-records> (140 characters max)>' , "
                "'notorious-for': ['', '', ... (05 itens max)] , "
                "'keywords': ['', '', ... (05 itens max)] }} , "
                "'political-experience': [political role (1999-2099)] | 'Unknown', 'endorsements': [endorsements] | 'Unknown', "
                "'funding-sources': [funding-sources] | 'Unknown'}}, ['SOURCE's URL 1', ..., 'SOURCE's URL N']]."
            ).format(candidate_name=candidate, country=election.country.label)
            candidate_data = get_full_data_from_candidate(candidate_profile_a)
            # print(candidate_data)
            candidate_full_data.append(candidate_data)

            # if candidate_data:
            #     # Optionally assign an ID if not present
            #     candidate_data['id'] = candidate_id
            #     candidate_id += 1

            #     candidate_full_data.append(candidate_data)
            # else:
            #     print(f"Failed to retrieve data for candidate: {candidate}")


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
            'candidate': candidate_full_data,
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