
import os
import csv
import pandas as pd

budget_data = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    #csv_header = next(csvfile)
    #print(f"Header: {csv_header}")


    # Read through each row of data after the header
    for row in csvreader:
        print(row)
        #print(row[0])

        #AAA ***** The total number of months included in the dataset
        row_count = sum(1 for row in csvreader)
        print("There are " + str(row_count) + " months of data")


#BBB ***** The total net amount of "Profit/Losses" over the entire period
        #total = 0
#print col # for troubleshooting
        #for col in row[1]:
        #        total += (col)
        #        print(total)

        #Net_P_L = pd.read_csv(budget_data.csv)
        #NetPandL = pd.read_csv(budget_data)
        ##NetandL[Net_P_L.columns[2].sum()
        #print(NetPandL)



#print("OK!! - we got to the end")
#print("OK, got to the end")