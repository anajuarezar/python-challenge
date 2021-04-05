import os
import csv

pybank_path = os.path.join('Resources', 'Lessons_03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

with open(pybank_path, newline='') as pybankfile:
    reader = csv.reader(pybankfile, delimiter=",")
