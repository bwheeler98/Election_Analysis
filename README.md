# Election_Analysis

## Project Overview
The Colorado Board of Elections has tasked us with analyzing the recent local congressional election reults.  We needed to find the following information:
  1.  Calculate the total number of votes cast.
  2.  Get a complete list of candidates who received votes.
  3.  Calculate the total number of votes each candidate received.
  4.  Calculate the percentage of votes each candidate recieved.
  5.  Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Python & Visual Studio Code

## Summary
The analysis of the shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
The Colorado Board of Election also wanted to analyze the voter turnout for each county in order to see which county had the largest turnout.  We needed to find the following information:
  1. Each county that had voters.
  2. The percentage of votes cast in each county out of the total votes.
  3. The county that had the largest percentage of voter turnout.

## Challenge Summary
There were 3 counties that had votes cast in the election.
-Jefferson County had 10.5% of the votes (38855)
-Denver County had 82.5% of the votes (306055)
-Arapahoe County had 6.7% of the votes (24801)

-Denver County had the largest turnout with 82.5%!

## Election-Audit Summary
This script is a great resource to use for election audits and can be replicated for other elections.  The script can be modified to use on a wider scale such as a national election.  You would need to then create a few new variable as well as a new dictionary to hold each state as the key and the county or counties within that state as the values.  Another modification for this script is if you were to use a different winning vote method such as plurality vote instead of popular vote.  For that modification you would need to alter the conditional and decision statements to calculate the true winner based on plurality vote, which is not as simple as the popular vote.
