# Program that reads a csv file as a Dictionary object
# Author: Oksana Abrosimova
import csv

filename = "data.csv"
datadir = "../data/"
fullpath  = datadir + filename

with open (fullpath, "rt") as fp: 
    reader = csv.DictReader(fp,delimiter=',',quoting=csv.QUOTE_NONNUMERIC) # function that reads csv file
    total = 0
    line_count = 0
    for line in reader: 
        total += line['age'] # no need to convert to int, quoting does it, i.e. csv.QUOTE_NONNUMERIC
        line_count += 1
    # First line is assumed to contain the keys to use to build the dictionary, 
    # so no need to skip it
    print(f"average is {total/(line_count)}")

