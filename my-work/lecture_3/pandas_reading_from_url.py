# Program that reads a csv file from a url using pandas
# Author: Oksana Abrosimova

import pandas as pd

# took URL from the web and added the last parameter &format=csv
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&format=csv"
# use a different protoco (need to pip install S3fs)

#url = "s3://noaa-gsod-pds/2020/72278023183.csv"

df = pd.read_csv(url)
print(df.head)