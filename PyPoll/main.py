import os
import csv


poll_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

with open(poll_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    first_row = next(reader)
    totalvotes = len(list(reader))


with open(poll_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    poll_dict = {}
    khan = []
    for row in reader:
        key = row[2]
        poll_dict[key] = row[1:]






    
    


print("Elections Results")
print("--------------------------------")
print(f"Total Votes: {totalvotes}")
print("--------------------------------")
Print(f"Khan: {khan_count}")
