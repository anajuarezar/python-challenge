#We begin with the environment activated.
# Then we import the modules we will be using to read de csv file. 
import os
import csv

#We make a secure path for the file. 

pybank_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

#Then we bring the file and specify the delimitations. 

with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    totalmonth = len(list(reader))

  

with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    profit = 0
    for line in reader:
        profit = profit + int(line[1])


with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #Discard header
    next(reader)
    first_row = next(reader)
    preview_val = int(first_row[1])
    lowest_profit = {"date": first_row[0] , "profit": int(first_row[1])}
    highest_profit = {"date": first_row[0], "profit": int(first_row[1])}
    profitlist = []
    for line in reader:
        change_profit = int(line[1]) - preview_val
        if change_profit < lowest_profit["profit"]:
            lowest_profit["date"] = line[0]
            lowest_profit["profit"] = change_profit
        preview_val = int(line[1])
        profitlist.append(change_profit)
    

    average = sum(profitlist) / len(profitlist)


with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    first_row = next(reader)
    preview_val = int(first_row[1])
    highest_profit = {"date": first_row[0], "profit": int(first_row[1])}
    profitlist = []
    print(first_row)
    for line in reader:
        change_profit = int(line[1]) - preview_val
        if change_profit > highest_profit["profit"]:
            highest_profit["date"] = line[0]
            highest_profit["profit"] = change_profit
        preview_val = int(line[1])
        profitlist.append(change_profit)

  

       

# Because every row is a different month, we can count the rows in order to find out how many months there are. 
    
    

#To know the total of profits and losses. We first need to start the count

    

    



       


 
#We print everything. 
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${profit}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profit: {highest_profit['date']} {highest_profit['profit']}")
print(f"Greatest Decrease in Profit: {lowest_profit['date']} {lowest_profit['profit']}")

