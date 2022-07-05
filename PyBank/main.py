# Module for creating file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join('PyBank\Resources', 'budget_data.csv')

# Lists to store data
total_months = []
total_profit = []
monthly_profit_change = []

# Open the CSV
with open(csvpath, encoding = "utf-8") as budget:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget, delimiter = ",")

    # Read the header row first (skip this step if there is row header)
    csvheader = next(csvreader)

    # Iterate through each row in the CSV
    for row in csvreader:

        # Add total months
        total_months.append(row[0])

        # Add net total
        total_profit.append(int(row[1]))
    
    # Iterate through profits to obtain monthly change in profits
    for i in range(len(total_profit) - 1):

        # Take difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i + 1] - total_profit[i])

# Get max and min of monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to proper month using month list and index from max and min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Open the output file
output_path = os.path.join('PyBank\Analysis', 'Financial_Analysis_Summary.txt')
with open(output_path, 'w') as csvfile:
    csvfile.write("Financial Analysis")
    csvfile.write("\n")
    csvfile.write("----------------------------")
    csvfile.write("\n")
    csvfile.write(f"Total Months: {len(total_months)}")
    csvfile.write("\n")
    csvfile.write(f"Total: ${sum(total_profit)}")
    csvfile.write("\n")
    csvfile.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    csvfile.write("\n")
    csvfile.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    csvfile.write("\n")
    csvfile.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")