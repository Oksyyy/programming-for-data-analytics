# program that reads a file and prints its content
# Author: Oksana Abrosimova

filename = "numbers.txt"
datadir = "../data/"
fullpath  = datadir + filename

#print(fullpath)

with open(fullpath, "rt") as fp:
    total = 0
    for line in fp:
        #print(f" {line.strip()}", end="")
        #print(f" has length {len(line.strip())}")
        total += int(line)
    print(total)