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

#We begin the process to find the profit  

with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
#We set the count to start at 0
    profit = 0
#We go line by line to slowly build the profit variable
    for line in reader:
        profit = profit + int(line[1])

#We begin again to find the max and min values

with open(pybank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
 #Discard header
    next(reader)
 #We create a variable that fixes the first row to compare it. 
    first_row = next(reader)
    preview_val = int(first_row[1])
#We create a dictionary so we can use it to retrieve the date and the profit
    lowest_profit = {"date": first_row[0] , "profit": int(first_row[1])}
#We create an empty list so we can append the values there. 
    profitlist = []
#We go line by line. 
    for line in reader:
#To find the change we must sustract the previous value to the current one. This is why we fixed that value. 
        change_profit = int(line[1]) - preview_val
#We compare the change we found before to the current profit in order to find the minimum change.
        if change_profit < lowest_profit["profit"]:
            lowest_profit["date"] = line[0]
            lowest_profit["profit"] = change_profit
        preview_val = int(line[1])
#We append the change in profit to the list profitlist. 
        profitlist.append(change_profit)
    
#Once we have the list, we find the average with the sum of the list and the lenght of the list.
    average = round(sum(profitlist) / len(profitlist), 2)

#We do the same to find max value. 
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


 
#We print everything. 
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${profit}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profit: {highest_profit['date']} ({highest_profit['profit']})")
print(f"Greatest Decrease in Profit: {lowest_profit['date']} ({lowest_profit['profit']})")

#We create the output file with put financial analysis

output_path = os.path.join("Analysis", "bank_result.csv")
with open (output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow([f"Total Months: {totalmonth}"])
    csvwriter.writerow([F"Total: ${profit}"])
    csvwriter.writerow([f"Average Change: ${average}"])
    csvwriter.writerow([f"Greatest Increase in Profit: {highest_profit['date']} ({highest_profit['profit']})"])
    csvwriter.writerow([f"Greatest Decrease in Profit: {lowest_profit['date']} ({lowest_profit['profit']})"])