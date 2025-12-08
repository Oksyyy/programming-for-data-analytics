# A program to demonstrate getting data from a URL using the requests object
# Author: Oksana Abrosimova

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)

# analyse data

#for event in data['northern-ireland']['events']:
    #print(f'{event}')
    #print(f'{event["title"]} is on {event["date"]}')

uk_unique_events = set()
for event in data['events']:
    uk_unique_events.add(event["title"])
    # print(f'The UK bank holidays are: {uk_unique_events}')
ni_only = set()
for event in data['northern-ireland']['events']:
    ni_only.add(event["title"])
    print(f'The UK bank holidays unique to Northern Ireland are: {ni_only}')
ni_only.add(data['northern-ireland']['event']["title"])
#print(f'The UK bank holidays unique to Northern Ireland are: {ni_only}')


