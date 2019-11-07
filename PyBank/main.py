import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
file_to_output = os.path.join("analysis", "budget_analysis.txt")

total_months = 0
prev_revenue = 0
total_revenue = 0
month_of_change = []
revenue_change_list =[]
greatest_increase = ['',0]
greatest_decrease = ['', 9999999999999999999999]


with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    
for row in csvreader:
    total_months = int(total_months) + 1
    
    total_revenue = 
