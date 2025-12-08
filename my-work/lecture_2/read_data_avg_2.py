# Program that reads a csv file and calculates average age
# Author: Oksana Abrosimova
import csv

filename = "data.csv"
datadir = "../data/"
fullpath  = datadir + filename

with open (fullpath, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC) # function that reads csv file
    line_count = 0
    total = 0
    for line in reader:
        if not line_count: # skip header
            pass
        else: 
            total += line[1] # no need to convert to int, quoting does it, i.e. csv.QUOTE_NONNUMERIC
        line_count += 1
    print(f"average is {total/(line_count-1)}")
