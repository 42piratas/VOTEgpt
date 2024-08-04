import ast
from decouple import config
from openai import OpenAI

# Initialize the OpenAI API client
client = OpenAI(
    api_key=config('OPENAI_API_KEY'),
)

# The following strings are used in the chatbot's prompts to guide the user on how to format their responses.
sources_strict: str = "Refer only to the following sources: International Foundation for Electoral Systems (IFES), ElectionGuide.org, Inter-Parliamentary Union (IPU), and International IDEA."
sources_reliable: str = "Ensure the data is sourced from reliable, impartial sources, such as academic publications, official electoral bodies, government reports, reputable non-partisan organizations, International Foundation for Electoral Systems (IFES), ElectionGuide.org, Inter-Parliamentary Union (IPU), and International IDEA."

# The following functions send requests to the GPT-4 model to verify the democratic status of a country
def verify_democratic(country):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Please, respond with only 'TRUE' or 'FALSE': is "+country+" democratic or not? Format the response as follows: [TRUE|FALSE, ['Source 1's URL', ..., 'Source N's URL']]. "+sources_strict,
            },
        ],
    )
    data = completion.choices[0].message.content
    print("Data democratic: ", data)
    data = data.replace("TRUE", "True")
    data = data.replace("FALSE", "False")
    data_list = ast.literal_eval(data)
    
    return data_list

# The following functions send requests to the GPT-4 model to get the elections scheduled for a country for the next 6 months
def get_country_elections(country):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Please, check if "+country+" has any elections scheduled for any time in the next 6 months, given today's date. If there are, list the types of elections (e.g., 'Presidential', 'Parliamentary', 'State', etc.), the scheduled dates for these elections, and provide the sources of this information. Format the response as follows: '[{{'Type of Election 1':'Date 1', 'Type of Election 2':'Date 2'}}, ['Source 1's URL', ..., 'Source N's URL']] or [FALSE, ['Source 1's URL', ..., 'Source N's URL']]. "+sources_strict,
            },
        ],
    )
    data = completion.choices[0].message.content
    print("Data elections: ", data)
    if data[0] != '[':
      return data
    data = data.replace("TRUE", "True")
    data = data.replace("FALSE", "False")
    data_list = ast.literal_eval(data)
    return data_list

def get_candidates_by_country_and_election(country, election_type, election_date):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Please, provide a list of the full names of all candidates participating in the upcoming "+election_type+" elections in "+country+" in "+election_date+" Format the response as follows: ['"+country+"', '"+election_type+"', '"+election_date+"', ['Full Name 1', 'Full Name 2', ..., 'Full Name N'], ['Source 1's URL', ..., 'Source N's URL']]. Include only the candidates' full names and the sources in the list. "+sources_reliable,
            },
        ],
    )
    data = completion.choices[0].message.content
    if data[0] != '[':
      return data
    data_list = ast.literal_eval(data)
    return data_list