import os

csvpath = os.path.join('Resources', 'election_data')

import csv

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='')

print(csvreader)
