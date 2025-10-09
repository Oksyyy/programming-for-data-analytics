# Program that reads in json data and prints the dates of the bank holidays happening in Northern Ireland
# Author: Oksana Abrosimova

import requests 

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# Get all events in Northern Ireland
ni_events = data["northern-ireland"]["events"][:]
event_count = 0
for event in ni_events:
    print(f' The date of {event["title"]} is {event["date"]}') 
    event_count += 1

