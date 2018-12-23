#import modules
import csv
import os
import sys
import pandas as pd
#import CSV
PyBank_Data = os.path.join("budget_data.csv")
#file_to_output = os.path("budget_analysis.txt")


# Track various financial parameters
earnings = []
months = []
Difference = []
bank_dict = {}
netTotal = 0
Average = 0
greatest_profit = 0
greatest_Loss = 0
#Read CSV
with open (PyBank_Data, newline= "") as PyBankFile:
    csvreader = csv.reader(PyBankFile,delimiter=",")
    BankHead = next(csvreader)

#create 4 Loop for total & Average
    for row in csvreader:
        netTotal += int(row[1])
        months.append(row[0])
        earnings.append(row[0])
    for i in range(1, int(len(months))):
        Difference.append(int(earnings[i]) - int(earnings[i-1]))
        Average = sum(Difference) / int(len(months) -1)

#Max & Min Calc 
    greatest_increase = max(Difference)
    greatest_profit = months[Difference.index(max(Difference))+1]
    greatest_decrease = min(Difference)
    greatest_loss = months[Difference.index(min(Difference))+1]

#print Results 
 
    PyBankResults = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${netTotal}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_profit[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_Loss[1]})\n")

    print(PyBankResults)

#f=open('Bank_data.txt','w')
#f.write(PyBankResults)
#f.close()

with open(Bank_data.txt, "w") as txt_file:
    txt_file.write(PyBankResults)


