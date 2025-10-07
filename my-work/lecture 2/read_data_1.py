# Program that reads a csv file and outputs each line as list
# Author: Oksana Abrosimova
import csv

filename = "data.csv"
datadir = "../data/"
fullpath  = datadir + filename

with open (fullpath, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",") # function that reads csv file
    for line in reader:
        print(line)

