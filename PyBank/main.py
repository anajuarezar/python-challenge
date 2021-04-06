#We begin with the environment activated.
# Then we import the modules we will be using to read de csv file. 
import os
import csv

#We make a secure path for the file. 

pybank_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

#Then we bring the file and specify the delimitations. 

with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    totalmonth = len(list(reader))

  

with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    profit = 0
    for line in reader:
        profit = profit + int(line[1])


with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    profitlist = []
    for line in reader:
        profitlist.append(int(line[1]))
        max_profit = max(profitlist)


  

       

# Because every row is a different month, we can count the rows in order to find out how many months there are. 
    
    

#To know the total of profits and losses. We first need to start the count

    

    



       


 
#We print everything. 
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${profit}")
print(f"Greatest Increase in Profit: {max_profit}")
