sources_strict = "Refer only to the following sources: International Foundation for Electoral Systems (IFES), ElectionGuide.org, Inter-Parliamentary Union (IPU) and International IDEA."

sources_reliable = "Ensure the data is sourced from reliable, impartial sources, such as academic publications, government reports, and reputable non-partisan organizations."

clean_output = "Don't add {candidate_name}'s name to the answer. Return only the requested information without any introduction, additional comments, or unnecessary text."

cite_sources =

scheduled to this year in the future based on today's date, <NOW-DATE>

what elections are scheduled to this year in the future based on today's date, 13 July 2024

return me a list with the name of all candidates running for <the presidential election in Venezuela>
Only use information from the sources below and from their government's official government --
International Foundation for Electoral Systems (IFES), ElectionGuide.org, Inter-Parliamentary Union (IPU)
and International IDEA. Also, return the source(s) you got the information from. Return only the list of candidates,
concisely, without introduction or any extra information or comments. Sources that delivered only
redundant information should not be listed.

candidates_experience = "Please, list {candidate_name}'s, the {candidate_nationality} candidate, previous political roles with dates, formatted as: '- Role (1999-2099)'"

candidates_experience += " " + sources_reliable + " " + cite_sources

candidate_keywords = "Please, return the 5 keywords that best describe {candidate_name}, the {candidate_nationality} candidate. Exclude any words related to professional roles, titles, or positions, such as 'politician', 'president', 'minister', etc."

candidate_lgbtq = "In 140 characters-max, what's {candidate_name}'s, the {candidate_nationality} candidate, position on LGBTQ rights?"

candidate_lgbtq += " " + sources_reliable + " " + clean_output + " " + cite_sources

candidate_lgbtq_sum = "Please, describe {candidate_name}'s, the {candidate_nationality} candidate, position on LGBTQ rights as either: 'SUPPORTIVE', 'OPPOSED', 'NEUTRAL', 'AMBIGUOUS', or 'UNKNOWN'."

candidate_lgbtq_sum += " " + sources_reliable + " " + clean_output + " " + cite_sources
