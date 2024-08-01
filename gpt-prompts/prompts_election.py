from prompts_common import *


####### CANDIDATES
####### E.G.
# [‘United States’, ‘Presidential’, ‘2024-11-05’, [‘Joe Biden’, ‘Donald Trump’, ‘Chase Oliver’, ‘Robert F. Kennedy Jr.’, ‘Ron DeSantis’,  ‘Cornel West’], [‘Ballotpedia’, ‘Wikipedia’]]

election_candidates: str = (
    "Please, provide a list of the full names of all candidates participating in the upcoming "
    "{election_type} elections in {country} in {election_date}. "
    "Format the response as follows: "
    "['{country}', '{election_type}', '{election_date}', ['Full Name 1', 'Full Name 2', ..., 'Full Name N'], ['Source 1', ..., 'Source N']]. "
    "Include only the candidates' full names and the sources in the list."
).format(country=country, election_type=election_type, election_date=election_date)

election_candidates += " " + sources_reliable
