import requests
import json
import pprint
from datetime import datetime
from newsapi import NewsApiClient

print(
    'Welcome to the Covid-19 data center. You can use this platform to access live and valuable information about COVID-19 developements across the world.')

# asks the user for the country that they are interested in
def CountryInput():
    print('What country are you interested in?')
    country = input()
    return country


country = CountryInput()

# Corona Virus API URL
url = 'https://api.covid19api.com/live/country/' + country


# Breaks the JSON code into more readable information
req = requests.get(url)
parsed = json.loads(req.text)

# added all relevant cases and their statuses
cases = parsed
date = datetime.today().strftime('%Y-%m-%d')
date = date + 'T00:00:00Z'
confirmed = 0
active = 0
recovered = 0
deaths = 0
for city in parsed:
    if city['Date'] == date:
        confirmed += city['Confirmed']
        active += city['Active']
        recovered += city['Recovered']
        deaths += city['Deaths']

# print(confirmed)


print("************************************************")
print('Corona Virus Cases in', country)
print('* Confirmed Cases:', confirmed)
print('* Active Cases:', active)
print('* Recovered Cases:', recovered)
print('* Deaths:', deaths)
print('Would you like to read articles about Covid-19 in', country, '(y/n)')

# Begining of the news segment of the code
NewsOption = input()

# URL and API key for the News API
newsapi = NewsApiClient(api_key='354411437b25453e90a5f324d649f9fe')

# print(country)
key_phrase = 'Corona AND ' + country
# print(key_phrase)
all_articles = newsapi.get_everything(q=key_phrase, domains='wsj.com, nytimes.com, bbc.co.uk, aljazeera.com')[
    'articles']

# for article in all_articles:

# Returns and prints the articles
if NewsOption == "y":

    if len(all_articles) > 0:
        for i in range(min(len(all_articles), 3)):  # determines how many results to show and what information to show
            print("**********************************************")
            print("Source: ", all_articles[i]['source']['name'])
            print("")
            print("Headline: ", all_articles[i]['title'])
            print("")
            print("Description: ", all_articles[i]['description'])
            print("")
            print("URL for article: ", all_articles[i]['url'])
            print("")
    else:
        print('Sorry there are no relevant articles.')
else:
    print('Thank you for visiting the Covid-19 Data Center')
