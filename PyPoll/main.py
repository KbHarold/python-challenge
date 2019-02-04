import os
import csv

#instructions on where to find the csv and assign it to the name poll_path
poll_path = os.path.join("Resources", "election_data.csv")

# Create variables for output
votes_cast = []
candidates = []
cand_names = []
winner =[]

with open(poll_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader:
        votes_cast.append(row[0])
        candidates.append(row[2])
    for candidate in candidates:
        if candidate not in cand_names:
            cand_names.append(candidate)

cand_1_votes = candidates.count(str(cand_names[0]))
cand_2_votes = candidates.count(str(cand_names[1]))
cand_3_votes = candidates.count(str(cand_names[2]))
cand_4_votes = candidates.count(str(cand_names[3]))

cand_tot_votes = [cand_1_votes,cand_2_votes,cand_3_votes,cand_4_votes]

cand_1_perct = (round((cand_1_votes / len(votes_cast))*100,3))
cand_2_perct = (round((cand_2_votes / len(votes_cast))*100,3))
cand_3_perct = (round((cand_3_votes / len(votes_cast))*100,3))
cand_4_perct = (round((cand_4_votes / len(votes_cast))*100,3))

cand_tot_perct = [cand_1_perct,cand_2_perct,cand_3_perct, cand_4_perct]

results = list(zip(cand_names,cand_tot_votes,cand_tot_perct))

for name in results:
    if max(cand_tot_votes) == name[1]:
        winner.append(name[0])


print("Election Results")
print("-----------------------------------")
print("Total Votes: ", len(votes_cast))
print("-----------------------------------")
print(f"{cand_names[0], cand_1_perct , cand_1_votes}")
print(f"{cand_names[1], cand_2_perct , cand_2_votes}")
print(f"{cand_names[2], cand_3_perct , cand_3_votes}")
print(f"{cand_names[3], cand_4_perct , cand_4_votes}")
print("-----------------------------------")
print("Winner: ", str(winner))
print("-----------------------------------")