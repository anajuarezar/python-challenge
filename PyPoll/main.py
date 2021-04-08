#We import the modules we will be using
import os
import csv


poll_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
    

with open(poll_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    totalvotes = 0
    candidates = []
    khan = []
    correy = []
    li = []
    tooley = []
    for row in reader:
        totalvotes = totalvotes + 1
        candidates.append(row[2])
        if row[2] == "Khan":
            khan.append(row[2])
        if row[2] == "Correy":
           correy.append(row[2])
        if row [2] == "Li":
            li.append(row[2])
        if row [2] == "O'Tooley":
            tooley.append(row[2])
    
    def winner_cand(candidates):
        return max(set(candidates), key = candidates.count)
    

    votes_khan = len(list(khan))
    votes_correy = len(list(correy))
    votes_li = len(list(li))
    votes_tooley = len(list(tooley))
    khan_percentage =round((votes_khan/totalvotes)*100, 2)
    correy_perc = round((votes_correy/totalvotes)*100, 2)
    li_perc = round((votes_li/totalvotes)*100, 2)
    tooley_perc = round((votes_tooley/totalvotes)*100, 2)
    winner = max(candidates)
    
    


print("Elections Results")
print("--------------------------------")
print(f"Total Votes: {totalvotes}")
print("--------------------------------")
print(f"Khan: {khan_percentage}% ({votes_khan})")
print(f"Correy: {correy_perc}% ({votes_correy})")
print(f"Li: {li_perc}% ({votes_li})")
print(f"O'Tooley: {tooley_perc}% ({votes_tooley})")
print("--------------------------------")
print(f"{winner_cand(candidates)}")