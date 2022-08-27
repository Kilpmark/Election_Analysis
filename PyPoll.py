# Retrieve Data
# Total number of votes cast
# List of all candidates who recieved votes
# Number of votes for each candidate
# Total vote for each candidate
# Percentage of overall total votes for each candidate
# Determine winner based on popular vote


# Import Statements

from ast import If
import csv

import os


# Assign variable name to file to load and path

file_to_load = os.path.join("Resources","election_results.csv")

# Creat filename variable for output

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total votes counter

total_votes = 0

# Initialize list of candidate names

candidate_options = []

# Dictionary with cand name as key and votes as value, initalization

candidate_votes = {}

# Winning candidate and count tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open file to read

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Perform Analysis

    # Use reader function from csv to read input file

    # Get Headers    
    headers = next(file_reader)

    # Print each row of input file

    for row in file_reader:

        #Add to total vote count

        total_votes += 1

        # Get Candidate name from each row

        candidate_name = row[2]

        # Add name to candidate options list

        if candidate_name not in candidate_options:

            # Add name to options list

            candidate_options.append(candidate_name)

            # Start tracking vote count

            candidate_votes[candidate_name] = 0
        
        # Add to current candidates vote count

        candidate_votes[candidate_name] += 1

    # Save results to text file

    with open(file_to_save,"w") as txt_file:

        # Print final vote count to terminal

        election_results = (
            f"Election Results\n"
            f"---------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n"
        )

        print(election_results, end="")

        # Save final vote count to file

        txt_file.write(election_results)

        # Determine percentage of total vote

        # Iterate through candidate list

        for candidate_name in candidate_votes:

            # Extract vote count for candidate

            votes = candidate_votes[candidate_name]

            # Calculate percentage

            vote_percentage = (float(votes)/float(total_votes))*100

            #Print candidates number of votes and percentage

            candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

            print(candidate_results)

            # Save to file

            txt_file.write(candidate_results)



            # Determine winning vote count and candidate

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

        #Output winner summary to terminal

        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count {winning_count:,}\n"
            f"Winning Percentage {winning_percentage:.1f}%\n"
            f"------------------------\n")

        print(winning_candidate_summary)
        
        # Add winning candidate summary to file

        txt_file.write(winning_candidate_summary)