# python-challenge
Python homework
python-challenge
Python homework This homework was divided into two projects: PyBank and PyPoll. 
PyBank: With this project, I began by activating the environment. After that, I imported the modules CSV and OS. 
CSV allows us to import, work with and export csv files. OS helps us secure the code even in different OS. Later, I created a secure path with os.join.path for my csvfile. 
Then, I imported the file and openeded it in read mode and determined the delimiters, in this case the ",". 
Once the file is opened, I used the function len to find the number of months in the file. However, I first isolated the header, so I could work with the data. 
After this, I began working on the profit. For this, I first created a counter that started in 0 so I could add the numbers there and eventually sum them. 
I had to cast the number as an integer in order to make operations. 
Later, I worked to find the maximum and minium. To do this I saved the first row as a variable thus using it to find the change in profit. 
I made a dictionary to facilitate the process of retrieving the date as well as an empty list to add the changes. We go through the loop, line by line, so we can make the sustraction and append the changes to the list. 
I used an if conditional to compare the values in order to find the smallest change. 
Once the profit list is done, I made the average with the len function again and round it to 2 decimals. I did the same with the maximum. 
Finally, I have the values I needed and because I used a dictionary I retrieved the date easily. 
I printed everything, but because I can only print string, I used the f-method to print my integers. 
Lastly I created a new file in write mode and printed there the analysis.

PyPoll:

I began PyPoll the same way: importing the modules and opening the file as a csvfile. I also isolated the header so I could work easily. 
I decided to use lists in this section. So I created empty lists for each candidate and an empty counter to find the number of votes. 
I went through the lines in a loop again adding the votes to the counter and appending the all the candidates to an emppty list. 
I then appended each candidate to its own list. I created a function to find the candidate with the most votes called winner_cand. 
I used len to find the number of votes each candidate had in their list and used the total votes list to find the percentages. I rounded this to 2 decimals.
I printed everything using the f-method and created a output file with the analysis.
