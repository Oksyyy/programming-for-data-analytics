# Preparing the population data for analysis
# Author: Oksana Abrosimova

import pandas as pd

filename = 'cso-populationbyage.csv'
datadir = '../data/'

fullpath = datadir + filename

# Read the csv file
df = pd.read_csv(fullpath)

# Drop unnecessary columns
drop_columns = ["Statistic Label","CensusYear","Sex","UNIT"]
df.drop(columns=drop_columns, inplace=True)
# another way to drop columns:
# df = df.drop(columns=drop_columns)

# Filter out rows where "Single Year of Age" is "All ages"
df= df[df["Single Year of Age"] != "All ages"]

# Replace "Under 1 year" with "0"
df["Single Year of Age"] = df["Single Year of Age"].str.replace("Under 1 year","0")
# Replace non-digit characters with an empty string
df["Single Year of Age"] = df["Single Year of Age"].str.replace("\D", "", regex=True)

# Check data types
# print(df.info()) 
# Convert the "Single Year of Age" column to integer type for further analysis
df["Single Year of Age"] = df["Single Year of Age"].astype(int)

# This is Andrew's version - didn't wrk for me
# df_analysis = df.pivot_table(df, 'VALUE', "Single Year of Age", "County and City")
# My version suggested by copilot
df_analysis = df.pivot_table(index='Single Year of Age', columns='County and City', values='VALUE')
print(df_analysis.head(3))


df_analysis.to_csv("population_for_analysis.csv")