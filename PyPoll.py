# The data we need to retrieve:

# Total number of votes cast
# The total number of votes cast across three counties was 369,711

# complete list of candidates who received votes
# The complete list of candidates who received votes in the election include:
# Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane

# Total number of votes each candidate received
# The total number of votes per candidate was:
# Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606
  
# Percentage of votes each candidate won
#Charles Casper Stockham: received 23.04854332167558% of the vote.
# Diana DeGette: received 73.81224794501652% of the vote.
# Raymon Anthony Doane: received 3.1392087333079077% of the vote.

# The winner of the election based on popular vote is Diana DeGette

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare empty dictionary
candidate_votes = {}    

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
       
        # Print the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0 

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Determine the percentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print the candidate name and percentage of votes.
            print(f"{candidate_name}: received {vote_percentage}% of the vote.")


# Print the candidate list.
print(candidate_votes) 