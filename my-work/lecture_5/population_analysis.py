# Analysis of population by age group using CSO data
# Author: Oksana Abrosimova

import pandas as pd

filename = 'population_for_analysis.csv'
datadir = './'

fullpath = datadir + filename

# Read the csv file
df = pd.read_csv(fullpath)
# print(df.head(3))

 # Exclude the first column which is 'Single Year of Age', leaving only counties
headers = df.columns[1:]  

# Select a distrct (Carlow) for analysis
district = headers[0]  
print (df[district].describe) 
# Since the values represent count of people in each age group, we can need to use weighted average for mean calculation

