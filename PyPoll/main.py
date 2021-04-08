#We import the modules we will be using
import os
import csv

#We create a secure path for the file.
poll_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
    
#We create a reference and we open the file to read as a csvfile with those parametres.
with open(poll_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
#we isolate the header
    header = next(reader)
#We create empty lists for each candidate and start the counter for the votes at cero.
    totalvotes = 0
    candidates = []
    khan = []
    correy = []
    li = []
    tooley = []
#We loop through the rows.
    for row in reader:
#We begin counting the votes as we go through the rows and we append the canditates to a list.
        totalvotes = totalvotes + 1
        candidates.append(row[2])
#We fill the lists with each candidate so we can letter count them. 
        if row[2] == "Khan":
            khan.append(row[2])
        if row[2] == "Correy":
           correy.append(row[2])
        if row [2] == "Li":
            li.append(row[2])
        if row [2] == "O'Tooley":
            tooley.append(row[2])

#We create a function to find the candidate with the highest count of votes. 
    def winner_cand(candidates):
        return max(set(candidates), key = candidates.count)
 
#We count the votes for each candidate in their lists. 
    votes_khan = len(list(khan))
    votes_correy = len(list(correy))
    votes_li = len(list(li))
    votes_tooley = len(list(tooley))

#Once we obtained the total votes for each candidate, we can calculate the percentages and round them to 2 decimals. 
    khan_percentage =round((votes_khan/totalvotes)*100, 2)
    correy_perc = round((votes_correy/totalvotes)*100, 2)
    li_perc = round((votes_li/totalvotes)*100, 2)
    tooley_perc = round((votes_tooley/totalvotes)*100, 2)
    
    
#We print the results. 

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