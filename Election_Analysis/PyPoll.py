# the data we need to retrieve 
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
#1. the total number of votes cast

#2. a complete list of candidates who received votes

#3. the percentage of votes each candidate won

#4. the total number of votes each candidate won

#5. the winner of the election based on popular vote
