import os
import csv

csvpath = os.path.join('C:', 'Users', 'Angie', 'Documents', 'GitHub', 'RU-JER-DATA-PT-10-2019-U-C', 'Homework', '03-Python Homework', 'PyBank,Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(cvsfile, delimiter=',')
    
