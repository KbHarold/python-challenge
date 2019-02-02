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

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader:
        months.append(row[0])
        tot_prof_loss.append(int(row[1]))
    for i in range(1, len(months)):
        prof_chg.append(tot_prof_loss[i] - tot_prof_loss[i-1] )
        aver_chg = sum(prof_chg) / len(prof_chg)
        grt_inc = max(prof_chg)
        grt_dec = min(prof_chg)
        grtst_date = str(months[prof_chg.index(max(prof_chg))+1])
        smlst_date = str(months[prof_chg.index(min(prof_chg))+1])

print("Financial Analysis")
print("-----------------------------------")                
print("Total Months:", len(months))
print("Total: $", sum(tot_prof_loss))
print("Average  Change: $ ",aver_chg)
print("Greatest Increase in Profits: ", grtst_date, grt_inc)
print("Greatest Increase in Profits: ", smlst_date, grt_dec)

