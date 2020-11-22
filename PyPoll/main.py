import os
import csv

total_votes = 0
candidate_choice = []
candidate_votes = []

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
analysispath = os.path.join("PyPoll", "Analysis", "PyPoll_Analysis.txt")
#   read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #total_votes = len(list(csvreader))
    #print(total_votes) #should be 3521002
  
#   Count number of votes cast
    for row in csvreader:

       total_votes += 1 #count votes
#   retrieving candidates
       candidate_name = (row[2])


#   Caculate percentage and winner
       if candidate_name in candidate_choice:
           candidate_index = candidate_choice.index(candidate_name)
           candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else: 
            candidate_choice.append(candidate_name)
            candidate_votes.append(1)

for candidate in candidate_votes
    votes = candidate_votes.get(candidate)
    vote_share = float(votes) / float(total_votes) *100

    if (votes > winning_count):
        winning_count = votes
        winner = candidate

    vote_results = f'{candidate}: {vote_share}% ({votes})\n'
    

    print("-------------------------\n")
    print("Election Results\n")
    print("-------------------------\n")
    print(f'"Total Votes: {total_votes}\n")
    print("-------------------------\n")
    print("vote_results")
    print("-------------------------\n")
    print(f'"Winner: {winner}\n")
    print("-------------------------\n")

with open(analysispath, "w", newline="")  as txtfile
    txtfile.write("-------------------------\n")
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f'"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    txtfile.write("vote_results\n")
    txtfile.write(f'"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

txt_file.write(txtfile)
 







#   Percentage of votes per candidate
#for "Candidate" in csvreader:
 #   if "Candidate" == "Khan":    
  #      khan_vote_percentage 
   #     print(row)




