#import modules
import os
import csv

csvpath = os.path.join('C:/Users/Angie/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv')
# Reading using CSV module

Total_voters = 0
Khan_votes = 'Khan'
Correy_votes = 'Correy'
Li_votes = 'Li'
OTooley_votes = 'O\'Tooley'
KhanVotes_list = 0
CorreyVotes_list = 0
LiVotes_list = 0
OTooleyVotes_List = 0
Winner_List =[]

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        Total_voters += 1
        
        # Count the votes of each candidate by name of Candidate and add it to the winners list to find highest number
        if row[2] == Khan_votes:
            KhanVotes_list += 1
            Winner_List.append(KhanVotes_list)
        if row[2] == Correy_votes:
            CorreyVotes_list += 1
            Winner_List.append(CorreyVotes_list)
        if row[2] == Li_votes:
            LiVotes_list += 1
            Winner_List.append(LiVotes_list)
        if row[2] == OTooley_votes:
            OTooleyVotes_List += 1  
            Winner_List.append(OTooleyVotes_List)
    
    print("Ellections Results")
    print("------------------------")
    print("Total Votes: " + str(Total_voters))
    print("------------------------")
    print(f"Khan: {round(((KhanVotes_list/Total_voters) * 100),3)}% ({KhanVotes_list})")
    print(f"Correy: {round(((CorreyVotes_list/Total_voters) * 100),3)}% ({CorreyVotes_list})")
    print(f"Li: {round(((LiVotes_list/Total_voters) * 100),3)}% ({LiVotes_list})")
    print(f"O\'Tooley: {round(((OTooleyVotes_List/Total_voters) * 100),3)}% ({OTooleyVotes_List})")
    print("------------------------")
    if max(Winner_List) == KhanVotes_list:
        print("Winner: Khan")
    if max(Winner_List) == CorreyVotes_list:
        print("Winner: Correy")
    if max(Winner_List) == CorreyVotes_list:
        print("Winner: Li")
    if max(Winner_List) == CorreyVotes_list:
        print("Winner: O\'Tooley")
    print("-------------------------")