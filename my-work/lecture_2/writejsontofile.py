# Practicing with json
# Author: Oksana Abrosimova
import json

data = {
    'name': 'Oksana',
    'age': 34,
    "student":True
 }

with open("silly.json", "w") as fp:
    # create a separate file called silly.json
    # indent puts "silly.json" into a nicer more readable fromat
    json.dump(data,fp, indent=4) 
json_string = json.dumps(data)
print(data)
print(json_string)