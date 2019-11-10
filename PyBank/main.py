import os
import csv

csvpath = os.path.join('budget_data.csv')
file_to_output = os.path.join("analysis", "budget_analysis.txt")

total_months = 0
prev_revenue = 0
total_revenue = 0
month_of_change = []
revenue_change_list =[]
greatest_increase = 0
greatest_month = ['']
greatest_decrease = 0
month_decrease = ['']

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # data = [row for row in csv.reader(csvfile)]
    # prev_revenue = int(data[0][1])
    prev_revenue = 867884
    
    for row in csvreader:
        if int(row[1])==prev_revenue:
        #Add Total Months
            total_months += 1
        #Add Profit/Losses
            total_revenue += int(row[1])

            continue
        #Add Total Months
        total_months += 1
        #Add Profit/Losses
        total_revenue += int(row[1])

        revenue_change_list = int(row[1]) - prev_revenue 
        
        month_of_change.append(revenue_change_list)
        
        prev_revenue = int(row[1])

        if int(row[1])>greatest_increase:
            greatest_increase = revenue_change_list
            greatest_month.append(row[0])

        if int(row[1])<greatest_decrease:
            greatest_decrease = revenue_change_list
            month_decrease.append(row[0])    

    print("Total Months:" + str(total_months))
    print("Total: $" + str(total_revenue))
    print("Average Change: $" + str(round(sum(month_of_change)/len(month_of_change),2)))
    print("Greatest increase in Profit: " + str(greatest_month[-1]) + " ($" + str(greatest_increase) +")")
    print("Greatest decrease in Profit "+ str(month_decrease[-1]) + " ($" + str(greatest_decrease) +")")