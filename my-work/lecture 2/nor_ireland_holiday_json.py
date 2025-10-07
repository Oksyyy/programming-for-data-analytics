# Program that reads in json data
# Author: Oksana Abrosimova

# when running a program call python3 (gives an error if used just python)
import requests 

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data["northern-ireland"]["events"][0])