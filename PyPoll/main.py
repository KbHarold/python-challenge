import os
import csv

#instructions on where to find the csv and assign it to the name poll_path
poll_path = os.path.join("Resources", "election_data.csv")

# Create variables for output
votes_cast = []
candidates = []
cand_names = []
winner =[]

#Open the CSV file and read the rows in to count the number of votes and collect the names voted for into a list
#After collecting the votes in the candidates list create another list to hold unique candidates names for comparison to votes
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

# Use the index of the unique candidates list to count the number of times it appears in tht total candidates list
cand_1_votes = candidates.count(str(cand_names[0]))
cand_2_votes = candidates.count(str(cand_names[1]))
cand_3_votes = candidates.count(str(cand_names[2]))
cand_4_votes = candidates.count(str(cand_names[3]))

# Create a new list of candiate votes organized by the index of the prior step
cand_tot_votes = [cand_1_votes,cand_2_votes,cand_3_votes,cand_4_votes]

# Calculate the percent of the vote each candidate by dividing it by the total votes
cand_1_perct = (round(((int(cand_1_votes) / int(len(votes_cast)))*100),2))
cand_2_perct = (round(((cand_2_votes / len(votes_cast))*100),2))
cand_3_perct = (round((cand_3_votes / len(votes_cast))*100,2))
cand_4_perct = (round((cand_4_votes / len(votes_cast))*100,2))

#Create a list of candidates percentage of votes
cand_tot_perct = [cand_1_perct,cand_2_perct,cand_3_perct, cand_4_perct]

#Combine the unique names, votes and percentage into a single list
results = list(zip(cand_names,cand_tot_votes,cand_tot_perct))

#Iterate over the combined list to find the winner and add to winner list
for name in results:
    if max(cand_tot_votes) == name[1]:
        winner.append(name[0])

#instructions to print the results of the election to the terminal
print("Election Results")
print("-----------------------------------")
print("Total Votes: ", int(len(votes_cast)))
print("-----------------------------------")
print(f"{cand_names[0]} {cand_1_perct}% ({cand_1_votes})")
print(f"{cand_names[1]} {cand_2_perct}% ({cand_2_votes})")
print(f"{cand_names[2]} {cand_3_perct}% ({cand_3_votes})")
print(f"{cand_names[3]} {cand_4_perct}% ({cand_4_votes})")
print("-----------------------------------")
print("Winner: ", str(winner).strip('[]'))
print("-----------------------------------")

#instructions to output results to an output folder in the form of a text file
output_path = os.path.join( "Output","Election_Results.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("-----------------------------------" "\n")
    txtfile.write("Total Votes: " + str(len(votes_cast)) + "\n")
    txtfile.write("-----------------------------------" "\n")    
    txtfile.write(str(cand_names[0])+ ": " + str(cand_1_perct)+ "% " +" " + "("+str(cand_1_votes)+")" + "\n")
    txtfile.write(str(cand_names[1])+ ": " + str(cand_2_perct)+ "% " +" " +"("+str(cand_2_votes)+")" + "\n")
    txtfile.write(str(cand_names[2])+ ": " + str(cand_3_perct)+ "% " +" " +"("+str(cand_3_votes)+")" + "\n")
    txtfile.write(str(cand_names[3])+ ": " + str(cand_4_perct)+ "% " +" " +"("+str(cand_4_votes)+")" + "\n")
    txtfile.write("-----------------------------------" "\n")
    txtfile.write("Winner : " +str(winner).strip('[]')+ "\n")
    txtfile.write("-----------------------------------" "\n")
    txtfile.close()