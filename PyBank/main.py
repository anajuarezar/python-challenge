#We begin with the environment activated.
# Then we import the modules we will be using to read de csv file. 
import os
import csv

#We make a secure path for the file. 

pybank_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

#Then we bring the file and specify the delimitations. 

with open(pybank_path) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
# We remove the header so it won't take it into consideration when it does any operations
    csv_header = next(csvfile)
# Because every row is a different month, we can count the rows in order to find out how many months there are. 
    totalmonth = len(list(reader))

#To know the total of profits and losses. We first need to start the counter
    profit = 0
    row = list(reader)
    
    for x in row:
        profit.append(row[1])
    
    total_profit = sum(profit)



       


 
#We print everything. 
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${total_profit}")