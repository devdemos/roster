# Weekly Roster 

## Requirements
Create a random weekly roster from a list of names, schedule a minimum of two persons once per week, and show that you can manage an odd number of names by choosing a different one from the list of ones you've already chosen. Permit the user to enter a start date and the name of the name file containing the names.

## About

### roster.py
A Python script that creates a weekly roster based on pairs using the input of a file containing a list of names and a date.
The output should be presented in tables with the week, date, and rostered pair information included.

The Roster script employs argparse to define two command-line arguments: names file and start date. The names file argument specifies the path to the CSV file that contains the names to be added to the roster. The start date argument specifies the start date for the weekly roster in the format "DD-MM-YYYY".

We parse the start date in the main function and pass the names file and start date to the create weekly roster() function.

The for loop that generates the weekly roster is set up to handle an odd number of items in the names file by using an if-else expression. The remaining name is appended to the roster if the index `i + 2` is more than the length of the names, at which point we choose the first name from the names list and add it to the roster for the current week.

The name is then removed from the names list to prevent further assignment. In this manner, even if the CSV file has an odd number of entries, at least two people will be added to the roster for each week.

### names.csv
A defualt CSV file that can contains a list of names to use as part of the roster.

## Run script 
You can run the script by using the command line and passing it the necessary arguments. As an example:

`python roster.py  names.csv 01-01-2023 -w 4`
This command will run the script, passing in the file path of the CSV file containing the names, the starting date in the format DD-MM-YYYY, the number of weeks to generate the roster for as 4, and the number of people to assign per week as 2 (the default value).

You can also specify the number of people per week while running the script:

`python roster.py names.csv 01-01-2023 -w 4 -n 3`

This command will run the script, passing in the file path of the CSV file containing the names, the starting date in the format DD-MM-YYYY, the number of weeks to generate the roster for as 4, and the number of people to assign per week as 3.

Please note that you have to provide the name of your script , the name of the csv file and the date in the format "DD-MM-YYYY" and the number of weeks.


```
Week | Date       | Names
-----|------------|------
   1 | 16/01/2023 | Person5 and Person2
   2 | 23/01/2023 | Person3 and Person1
   3 | 30/01/2023 | Person4 and Person5
```

## Limitations 
As currently written, the script is limited by the number of names in the CSV file. If the number of weeks specified by the user exceeds the number of possible pairings, the roster generates the maximum number of possible pairings rather than raising an error.