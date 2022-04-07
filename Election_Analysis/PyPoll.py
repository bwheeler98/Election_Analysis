# the data we need to retrieve 
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0
#candidate options
candidate_options =[]
#votes per candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #add to list of candidates
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #add vote to candidates count
        candidate_votes[candidate_name] +=1
#1. the total number of votes cast
#print(total_votes)
#2. a complete list of candidates who received votes
#print(candidate_options)
#3. the percentage of votes each candidate won
    #iterate through the candidate list
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #calculate the percentage
    vote_percentage = float(votes)/ float(total_votes) * 100
    #print the candidate name and percentage of votes
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    #print out each candidate's name vote count and percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#5.# the winner of the election based on popular vote
    #inside for loop determine if the votes are > winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n")
print(winning_candidate_summary)

#4. the total number of votes each candidate won
#print(candidate_votes)
