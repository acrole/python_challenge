import os

#csvpath = os.path.join("Resources/election_data")

import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        print(len(row))
        # print(len(list(row))) 'printed count of data in each line



