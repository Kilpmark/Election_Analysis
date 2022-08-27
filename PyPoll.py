# Retrieve Data
# Total number of votes cast
# List of all candidates who recieved votes
# Number of votes for each candidate
# Total vote for each candidate
# Percentage of overall total votes for each candidate
# Determine winner based on popular vote


# Import Statements

import csv

import os


# Assign variable name to file to load and path

file_to_load = os.path.join("Resources","election_results.csv")

# Creat filename variable for output

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open file to read

with open(file_to_load) as election_data:


    # Perform Analysis

    # Use reader function from csv to read input file

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    print(headers)

    # Print each row of input file

    #for row in file_reader:

     #   print(row)








# Use with statement for output file to write

#with open(file_to_save, "w") as txt_file:

    # Write data to file

 #   txt_file.write("")







