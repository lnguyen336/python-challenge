# Module for creating file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join('PyPoll\Resources', 'election_data.csv')

# Declare variables
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

# Open the CSV
with open(csvpath, encoding = "utf-8") as election:

    # CSV reader specifies delimiter and variable that holds content
    csvreader = csv.reader(election, delimiter = ",")

    # Read the header row first (skip this step if there is row header)
    csvheader = next(csvreader)

    # Iterate through each row in the CSV
    for row in csvreader:

        # Count unique voter IDs
        total_votes += 1

        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes += 1

# Create dictionary from lists previously created
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [charles_votes, diana_votes, raymon_votes]

# Zip the lists of candidates and total values together
dict_candidates_and_votes = dict(zip(candidates, votes))

# Return winner using max function of dictionary
key = max(dict_candidates_and_votes, key = dict_candidates_and_votes.get)

# Obtain percentage of votes each candidate won
charles_percent = (charles_votes/total_votes) * 100
diana_percent = (diana_votes/total_votes) * 100
raymon_percent = (raymon_votes/total_votes) * 100

# Print the Summary Table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Open the output file
output_path = os.path.join('PyPoll\Analysis', 'Election_Results_Summary.txt')
with open(output_path, 'w') as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")