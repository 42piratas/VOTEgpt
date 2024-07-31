from prompts_common import *


####### SHORTNAME
####### EX EXPECTED RETURN:
####### 'Lula'
####### - or -
####### 'FALSE'

candidate_shortname = (
    "Please provide the commonly used short name or nickname for the political candidate named {candidate_name}. "
    "Respond with only the short name or nickname. If there is no commonly used short name or nickname, respond with 'FALSE'."
).format(candidate_name=candidate_name)


####### EXPERIENCE

candidates_experience = "Please, list {candidate_name}'s, the {candidate_nationality} candidate, previous political roles with dates, formatted as: '- Role (1999-2099)'"å

candidates_experience += " " + sources_reliable + " " + cite_sources

####### KEYWORDS

candidate_keywords = "Please, return the 5 keywords that best describe {candidate_name}, the {candidate_nationality} candidate. Exclude any words related to professional roles, titles, or positions, such as 'politician', 'president', 'minister', etc."

####### LGBTQ

candidate_lgbtq = "In 140 characters-max, what's {candidate_name}'s, the {candidate_nationality} candidate, position on LGBTQ rights?"

candidate_lgbtq += " " + sources_reliable + " " + clean_output + " " + cite_sources

####### LGBTQ SUMMARY

candidate_lgbtq_sum = "Please, describe {candidate_name}'s, the {candidate_nationality} candidate, position on LGBTQ rights as either: 'SUPPORTIVE', 'OPPOSED', 'NEUTRAL', 'AMBIGUOUS', or 'UNKNOWN'."

candidate_lgbtq_sum += " " + sources_reliable + " " + clean_output + " " + cite_sources
