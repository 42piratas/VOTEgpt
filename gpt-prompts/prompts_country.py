from prompts_common import *


####### DEMOCRATIC
####### EX EXPECTED RETURN:
####### [TRUE, [‘IFES’, ‘ElectionGuide.org’]]

country_is_democratic = (
    "Please, respond with only 'TRUE' or 'FALSE': is {country} democratic or not? "
    "Format the response as follows: [<TRUE|FALSE>, ['Source 1', ..., 'Source N']]"
).format(country=country)

country_is_democratic += " " + sources_strict


####### ELECTIONS
####### EX EXPECTED RETURN:
####### [{'Parliamentary':'2024-04-10', 'Provincial':'2024-04-10'], ['International IDEA', 'ElectionGuide.org']]
####### - or -
####### ['FALSE', ['International IDEA', 'ElectionGuide.org']]

country_elections = (
    "Please, check if {country} has any elections scheduled for any time in the future. "
    "If there are, list the types of elections (e.g., ‘Presidential’, ‘Parliamentary’, ‘State’, etc.), "
    "the scheduled dates for these elections, and provide the sources of this information. "
    "Format the response as follows: "
    "[{{'Type of Election 1':'Date 1', 'Type of Election 2':'Date 2'}}, ['Source 1', ..., 'Source N']] or ['FALSE', ['Source 1', ..., 'Source N']]"
).format(country=country)

country_elections += " " + sources_strict
