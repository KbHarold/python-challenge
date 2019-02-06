import os
import csv

#instructions on where to find the csv and assign it the name budget_csv
budget_csv = os.path.join("Resources","budget_data.csv")

#create variables for output
months = []
tot_prof_loss = []
prof_chg = []
grt_inc = []
grt_dec = []

#Open the CSV file and read the rows in to count the number of months profit
#Also calculates the change since the prior month determine the greatest increase/decrease
#Also grabs dates of greatest increase and decrease based on index values for max/min
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader:
        months.append(row[0])
        tot_prof_loss.append(int(row[1]))
    for i in range(1, len(months)):
        prof_chg.append(tot_prof_loss[i] - tot_prof_loss[i-1] )
        aver_chg = round((sum(prof_chg) / len(prof_chg)),2)
        grt_inc = max(prof_chg)
        grt_dec = min(prof_chg)
        grtst_date = str(months[prof_chg.index(max(prof_chg))+1])
        smlst_date = str(months[prof_chg.index(min(prof_chg))+1])

#instructions to print the results of the election to the terminal
print("Financial Analysis")
print("-----------------------------------")                
print("Total Months:", len(months))
print("Total: $", sum(tot_prof_loss))
print("Average  Change: $",aver_chg)
print("Greatest Increase in Profits: ", grtst_date,"($", grt_inc,")")
print("Greatest Increase in Profits: ", smlst_date, "($", grt_dec,")")

#instructions to output results to an output folder in the form of a text file
output_path = os.path.join( "Output","Financial_Analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("-----------------------------------" "\n")
    txtfile.write("Total Months: " + str(len(months)) + "\n")
    txtfile.write("Total $ " + str(sum(tot_prof_loss)) + "\n")
    txtfile.write("Average  Change: $" + str(aver_chg) + "\n")
    txtfile.write("Greatest Increase in Profits: " + str(grtst_date) +" ($" + str(grt_inc)+") " + "\n")
    txtfile.write("Greatest Decrease in Profits: " + str(smlst_date) +" ($" + str(grt_dec)+") " + "\n")
    txtfile.close()