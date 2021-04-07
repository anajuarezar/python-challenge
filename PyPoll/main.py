import os
import csv


poll_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

with open(poll_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    first_row = next(reader)
    for row in reader:
        
    


with open(poll_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    poll = {}
    for row in reader:
        names_dict = row[2]
        poll[names_dict] = row[1:]
    

with open(poll_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    khan = []
    correy = []
    li = []
    tooley = []
    for row in reader:
        if row[2] == "Khan":
            khan.append(row[2])
        if row[2] == "Correy":
           correy.append(row[2])
        if row [2] == "Li":
            li.append(row[2])
        if row [2] == "O'Tooley":
            tooley.append(row[2])
    

    votes_khan = len(list(khan))
    votes_correy = len(list(correy))
    votes_li = len(list(li))
    votes_tooley = len(list(tooley))
    khan_percentage = (votes_khan/totalvotes)*100
    correy_perc = (votes_correy/totalvotes)*100
    li_perc = (votes_li/totalvotes)*100
    tooley_perc = (votes_tooley/totalvotes)*100




    
print(dict.keys(poll))








    
    


print("Elections Results")
print("--------------------------------")
print(f"Total Votes: {totalvotes}")
print("--------------------------------")
print(f"Khan: {khan_percentage}% ({votes_khan})")
print(f"Correy: {correy_perc}% ({votes_correy})")
print(f"Li: {li_perc}% ({votes_li})")
print(f"O'Tooley: {tooley_perc}% ({votes_tooley})")

