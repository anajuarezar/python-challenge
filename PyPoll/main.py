import os
import csv


poll_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

with open(poll_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    first_row = next(reader)
    totalvotes = len(list(reader))


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
    for row in reader:
        if row[2] == "Khan":
            khan.append(row[2])
    print(khan)


    
print(dict.keys(poll))








    
    


print("Elections Results")
print("--------------------------------")
print(f"Total Votes: {totalvotes}")
print("--------------------------------")

