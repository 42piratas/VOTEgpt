from prompts_common import *


####### SHORTNAME #######

# 'Lula'
# 'Joe Biden'
# FALSE

candidate_shortname: str = (
    "Please, provide the commonly used short name or nickname for the political candidate named "
    "{candidate_name} from {country}. "
    "Respond with only the short name or nickname. "
    "If there is no commonly used short name or nickname, respond with FALSE."
).format(candidate_name=candidate_name, country=country)


####### PROFILE A #######

# [{'born': ['Caetés, Brazil', '1945-10-27', 76],
# 'nationality': ['Brazilian'],
# 'religion': 'Roman Catholic',
# 'education': ['Primary Education'],
# 'current-party': ['Workers\' Party'],
# 'political-experience': ['President of Brazil (2003-2011)'],
# 'endorsements': 'Unknown',
# 'funding-sources': 'Unknown'},
# ['https://en.wikipedia.org/wiki/Luiz_In%C3%A1cio_Lula_da_Silva',
# 'https://www.britannica.com/biography/Luiz-Inacio-Lula-da-Silva']]

candidate_profile_a: str = (
    "Please, provide detailed information about the political candidate "
    "named {candidate_name} from {country}. "
    "Include the following details and return 'Unknown' for any information that is not available. "
    "Format the response as follows: "
    "{{'born': [location, date, age] | 'Unknown', 'nationality': [nationality(ies)] | 'Unknown', "
    "'religion': Religion | 'Unknown', 'education': [education] | 'Unknown', "
    "'current-party': [current-party] | 'Unknown', 'previous-party(ies)': [previous-party(ies)] | 'Unknown', "
    "'political-experience': [political role (1999-2099)] | 'Unknown', 'endorsements': [endorsements] | 'Unknown', "
    "'funding-sources': [funding-sources] | 'Unknown'}}, ['SOURCE's URL 1', ..., 'SOURCE's URL N']]."
).format(candidate_name=candidate_name, country=country)

candidate_profile_a += " " + sources_reliable


####### PROFILE B #######

# [{'biography': 'Luiz Inácio Lula da Silva, born in Caetés, Pernambuco, Brazil on October 27, 1945,
# is a former metalworker and trade unionist. He co-founded the Workers' Party in 1980 and was elected
# President of Brazil, serving from 2003 to 2011 and again from 2023. Lula is known for his social policies
# and economic reforms.',
# 'mini-biography': 'Brazilian president and Workers' Party founder, known for social and economic reforms.',
# 'platform': ['Economic growth', 'Social equity', 'Environmental sustainability',
# 'International cooperation', 'Anti-corruption'],
# 'criminal-records': 'Convicted of corruption and money laundering, served 580 days in prison.',
# 'notorious-for': ['Economic reforms', 'Bolsa Família program', 'Petrobras scandal',
# 'Trade union activism', 'Environmental policies'],
# 'keywords': ['Socialist', 'Reformer', 'Controversial', 'Unionist', 'Environmental advocate']},
# ['https://www.britannica.com/biography/Luiz-Inacio-Lula-da-Silva',
# 'https://en.wikipedia.org/wiki/Luiz_In%C3%A1cio_Lula_da_Silva',
# 'https://www.gov.br/planalto/en/biography-of-president-luiz-inacio-lula-da-silva']]

candidate_profile_b: str = (
    "Please, provide detailed information about the political candidate named "
    "{candidate_name} from {country}. "
    "Include the following details and return 'Unknown' for any information that is not available. "
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
    "['SOURCE's URL 1' , ... , 'SOURCE's URL N']]"
).format(candidate_name=candidate_name, country=country)

candidate_profile_b += " " + sources_reliable


####### PROFILE C #######

# {‘abortion': ‘Supports decriminalizing abortion and expanding women's reproductive rights.',
# ‘health-care': ‘Advocates for universal health care through the SUS, improving access and quality.',
# ‘economy': ‘Focuses on reducing inequality, increasing minimum wage, and progressive taxation.',
# ‘immigration': ‘Supports humane immigration policies and refugee rights.',
# ‘gun-control': ‘Advocates for stricter gun control laws to reduce violence.',
# ‘gun-control-short': ‘supportive',
# ‘climate-change': ‘Committed to ending deforestation by 2030 and promoting renewable energy.',
# ‘education': ‘Prioritizes expanding access to education and increasing funding.',
# ‘taxes': ‘Favors higher taxes on the wealthy to fund social programs.',
# ‘lgbtq-rights': ‘Supports LGBTQ rights and anti-discrimination policies.',
# ‘lgbtq-rights-short': ‘supportive',
# ‘foreign-policy': ‘Advocates for strong international cooperation on climate and economic issues.',
# ‘drug-policy': ‘Supports decriminalization of drug use and increased focus on treatment.',
# ‘criminal-justice-reform': ‘Advocates for reform to address systemic biases and reduce incarceration rates.',
# ‘military-spending': ‘Supports maintaining current levels with a focus on modernization.',
# ‘voting-rights': ‘Supports expanding voting access and combating voter suppression.'}

candidate_profile_b: str = (
    "Please, provide the public opinions/policies of the political candidate named "
    "{candidate_name} from {country} on the following topics. "
    "Each response should be limited to 140 characters, except for the 'short' fields, "
    "which should respond with one of the following: supportive, opposed, neutral, ambiguous, or unknown. "
    "If information is not available, return 'Unknown'. "
    "Format the response as follows: "
    "{{ "
    "'abortion': 'Policy on abortion (140 characters max)', "
    "'health-care': 'Policy on health-care (140 characters max)', "
    "'economy': 'Policy on economy (140 characters max)', "
    "'immigration': 'Policy on immigration (140 characters max)', "
    "'gun-control': 'Policy on gun-control (140 characters max)', "
    "'gun-control-short': 'supportive | opposed | neutral | ambiguous | unknown', "
    "'climate-change': 'Policy on climate-change (140 characters max)', "
    "'education': 'Policy on education (140 characters max)', "
    "'taxes': 'Policy on taxes (140 characters max)', "
    "'lgbtq-rights': 'Policy on lgbtq-rights (140 characters max)', "
    "'lgbtq-rights-short': 'supportive | opposed | neutral | ambiguous | unknown', "
    "'foreign-policy': 'Policy on foreign-policy (140 characters max)', "
    "'drug-policy': 'Policy on drug-policy (140 characters max)', "
    "'criminal-justice-reform': 'Policy on criminal-justice-reform (140 characters max)', "
    "'military-spending': 'Policy on military-spending (140 characters max)', "
    "'voting-rights': 'Policy on voting-rights (140 characters max)' "
    "}}"
).format(candidate_name=candidate_name, country=country)
