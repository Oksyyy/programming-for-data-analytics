# Program that reads in json data and outputs the 1st holiday in Northern Irland
# Author: Oksana Abrosimova

# when running a program call python3 (gives an error if used just python)
import requests 

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)