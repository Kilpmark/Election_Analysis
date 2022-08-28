# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

#Create a county list and county votes dictionary.

county_name = []
county_votes = {}



# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.

county_high_turnout = ""
county_high_turnout_votes = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.

        county = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Check that the current county does not match any existing county in the county list.

        if county not in county_name:

            # Append to list of names
            county_name.append(county)
            
            # Initialize vote count for current county
            county_votes[county] = 0
        
        # Add to current county's vote count
        county_votes[county] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n\n"
        f"County Results\n"
        f"-------------------------\n")

    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:

        # Get votes for current county

        votes_cast = county_votes[county]

        # Calculate % of total votes cast in current county

        votes_cast_percent = (float(votes_cast)/float(total_votes))*100

         # Print the county results to the terminal.
        county_out = f"{county} County: {votes_cast_percent:.1f}% ({votes_cast:,})\n"
        
        print(county_out)

        # Save the county votes to a text file.

        txt_file.write(county_out)

         # Determine highest turnout

        if votes_cast > county_high_turnout_votes:

            county_high_turnout_votes = votes_cast
            county_high_turnout = county




    # Print the county with the largest turnout to the terminal and title next section.
    high_turn = (f"Largest Turnout: {county_high_turnout} County\n"
    f"\nCandidate Results\n"
    f"--------------------------\n")
    print(high_turn)
    # Save the county with the largest turnout to a text file.
    txt_file.write(high_turn)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
