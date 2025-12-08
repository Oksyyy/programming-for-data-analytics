# program that reads a csv file and prints its content
# Author: Oksana Abrosimova
import csv

filename = "students.csv"
datadir = "../data/"
fullpath  = datadir + filename

#print(fullpath)

with open(fullpath, "rt") as fp: # fp = file pointer
    #for line in fp:
    #   print(line, end="")
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    line_number = 0
    for line in reader:
        if line_number: # skip the header line (0 is always falsy in Python, so it will skip the first line)
            total += int(line[1]) # ages have quotes so are read in as strings
        
        line_number += 1
    print(total)