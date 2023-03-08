#import
import os
import csv
import pandas as pd

#csv reader
budget_csv = "Py_Bank/budget_data.csv"
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_df = pd.read_csv("Py_Bank/budget_data.csv")
    total_months = 0
    total_profit = 0
    runtime = 0
    total_change = 0
    df = pd.read_csv('Py_Bank/budget_data.csv')

    max_value = df['Profit/Losses'].max()
    max_row = df.loc[df['Profit/Losses'] == max_value]

    min_value = df['Profit/Losses'].min()
    min_row = df.loc[df['Profit/Losses'] == min_value]

    budget_df["Change"] = budget_df["Profit/Losses"].diff()
    average_change = budget_df["Change"].mean()
    formatted_average_change = "%.2f" % average_change

    for i in csvreader:
        if runtime == 0:
            runtime += 1
        else:
            total_months += 1
            total_profit += int(i[1])  
            
    print(total_months)
    print(total_profit)
    print(formatted_average_change)
    print(max_row)
    print(min_row)

    with open("budget.txt", "w") as file:
        file.write("Financial analysis")
        file.write("----------------------------")
        file.write(f"Total Months: {total_months}")
        file.write(f"Total: {total_profit}")
        file.write("Average Change: {formatted_average_change}")
        file.write("----------------------------")
        file.write(f"Greatest Increase in Profits: {max_row}")
        file.write("----------------------------")
        file.write(f"Greatest Decrease in Profits: {min_row}")

