
import os
import csv
import sys
import pandas as pd

budget_data = os.path.join('..', 'Resources', 'budget_data.csv')
bank = pd.read_csv(budget_data, encoding="utf-8")

tot_months = 0
tot_revenue = 0
prev_rev = 0
mon_revenue_chng = 0
mon_revenue_chng_tot = 0
avg_mon_revenue_chng = 0
#max_mon_revenue_chng = 0
#min_mon_revenue_chng = 0    

# Open and read csv
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Read through each row of data after the header
    for rows in csvreader:
        tot_months = tot_months + 1

        if (tot_months == 1):
            prev_rev = int(rows[1])
        else:
            mon_revenue_chng = int(rows[1]) - prev_rev

        tot_revenue = tot_revenue + prev_rev
        mon_revenue_chng_tot = mon_revenue_chng_tot + mon_revenue_chng
        avg_mon_revenue_chng = mon_revenue_chng_tot / tot_months - 1

    print("There are " + str(tot_months) + " months of data")
    print("Total revenue for " + str(tot_months) + " months is " + str(tot_revenue))
    print("Average revenue change during the " + str(tot_months) + " months is " + str(avg_mon_revenue_chng))

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    max_mon_revenue_chng = 0
    min_mon_revenue_chng = 0    

    # Read through each row of data after the header
    for rows in csvreader:

        rows = list(csvreader) # now it's in memory, so we can reuse it
        max_mon_revenue_chng = max(rows, key=lambda row: int(row[1]))
        min_mon_revenue_chng = min(rows, key=lambda row: int(row[1]))

        print("The largest revenue increase is " + str(max_mon_revenue_chng))
        print("The largest revenue decrease is " + str(min_mon_revenue_chng))

bankoutput = os.path.join('C:/Users/tgmato/Documents/WashU_Data_Analytics_Boot_Camp/Python-Challenge/PyBank/Resources/bankoutput.csv')
with open(bankoutput, 'w', newline='') as csvfile:
    sys.stdout = csvfile
    print("There are " + str(tot_months) + " months of data")
    print("Total revenue for " + str(tot_months) + " months is " + str(tot_revenue))
    print("Average revenue change during the " + str(tot_months) + " months is " + str(avg_mon_revenue_chng))
    print("The largest revenue increase is " + str(max_mon_revenue_chng))
    print("The largest revenue decrease is " + str(min_mon_revenue_chng))
