import csv
import os

      #set path for read
election_csv = os.path.join("/Users/mother/mod_3_challenge/python-challenge/PyPoll/Resources/election_data.csv")
      
 # Create variable to store total count and dict to store candidate info
total_votes = 0
candidate_tot = {}

# Open the CSV file and read the candidate column
with open(election_csv, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Count total votes
        total_votes += 1
        candidate_name = row["Candidate"]

        # Check if the candidate is already in dict
        if candidate_name not in candidate_tot:
            candidate_tot[candidate_name] = 0

        # add votes
        candidate_tot[candidate_name] += 1

print(f"\nElection Results\n")
print("_" *26)

            # Print number of votes
print(f"\nTotal Votes: {total_votes:,}\n")
print('-' * 26)

            # figure and print 
for candidate, votes in candidate_tot.items():
    percentage = (votes / total_votes) * 100
    print(f"\n{candidate}: {percentage:.3f}% ({votes:,})\n")

print('-' * 26)

            #winner is...
winner = max(candidate_tot, key=candidate_tot.get)
print(f"\nWinner: {winner}\n")     
print('_'*26)

analysis_txt = open("/Users/mother/mod_3_challenge/python-challenge/PyPoll/analysis/analysis.txt", "w+")
analysis_txt.write(f"\nElection Results\n")
analysis_txt.write("_" *26)
analysis_txt.write(f"\nTotal Votes: {total_votes:,}\n")
analysis_txt.write('-' * 26)
for candidate, votes in candidate_tot.items():
    percentage = (votes / total_votes) * 100
    analysis_txt.write(f"\n{candidate}: {percentage:.3f}% ({votes:,})\n")
analysis_txt.write('-' * 26)
analysis_txt.write(f"\nWinner: {winner}\n")     
analysis_txt.write('_'*26)
