import os
import csv

election_csv = "Py_Poll/election_data.csv"
with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    total_votes = 0
    raymond_votes = 0
    diana_votes = 0
    charles_votes = 0
    candidates = set()
    for i in csvreader:
        total_votes += 1
        candidates.add(i[2]) 
        
        if i[2] == "Raymon Anthony Doane":
            raymond_votes += 1
        elif i[2] == "Diana DeGette":
            diana_votes += 1
        elif i[2] == "Charles Casper Stockham":
            charles_votes += 1
raymond_percentage = (raymond_votes / total_votes) * 100
formatted_raymond_percentage = "%.3f" % raymond_percentage
diana_percentage = (diana_votes / total_votes) * 100
formatted_diana_percentage = "%.3f" % diana_percentage
charles_percentage = (charles_votes / total_votes) * 100
formatted_charles_percentage = "%.3f" % charles_percentage
highest = max(charles_votes,diana_votes,raymond_votes)
if highest == charles_votes:
    winner = "Charles"
elif highest == diana_votes:
    winner = "Diana"
else:
    winner = "Raymond"

print("All candidates: ", candidates)
print("-------------------------")
print("Total votes: ", total_votes)
print("-------------------------")
print(f"Raymond Anthony Doane: {formatted_raymond_percentage}% ({raymond_votes})")
print(f"Diana DeGette: {diana_percentage}% ({diana_votes})")
print(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})")
print("-------------------------")
print(f"The winner of the election is {winner}!")

with open("election.txt", "w") as file:
    file.write("Election Results")
    file.write("----------------------------")
    file.write(f"Total votes: {total_votes}")
    file.write("-------------------------")
    file.write(f"Raymond Anthony Doane: {raymond_percentage}% ({raymond_votes})")
    file.write(f"Diana DeGette: {diana_percentage}% ({diana_votes})")
    file.write(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})")
    file.write("----------------------------")
    file.write(f"The winner of the election is {winner}!")