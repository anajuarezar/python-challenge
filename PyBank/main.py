#We begin with the environment activated.
# Then we import the modules we will be using to read de csv file. 
import os
import csv

#We make a secure path for the file. 

pybank_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

#Then we bring the file and specify the delimitations. 

with open(pybank_path) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    totalmonth = len(list(reader))

 

print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {totalmonth}")