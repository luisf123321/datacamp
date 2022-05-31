#csv

"""
Reading from a file using CSV reader
Python provides a wonderful module called csv to work with CSV files. 
You can pass the .reader() method of csv a Python file object and use it as you would any other iterable.
To create a Python file object, you use the open() function, which accepts a file name and a mode. 
The mode is typically 'r' for read or 'w' for write.

Though you won't use it for this exercise, often CSV files will have a header row with field names, 
and you will need to use slice notation such as [1:] to skip the header row.

You'll now use the csv module to read the baby_names.csv file and fill the baby_names dictionary with data. 
This baby_names dictionary has already been created for you.
"""

# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('baby_names.csv','r')

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary
    baby_names[row[5]] = row[3]

# Print the dictionary keys
print(baby_names.keys())

"""
Creating a dictionary from a file
The csv module also provides a way to directly create a dictionary from a CSV file with the DictReader class. 
If the file has a header row, that row will automatically be used as the keys for the dictionary. 
However, if not, you can supply a list of keys to be used. Each row from the file is returned as a dictionary. 
Using DictReader can make it much easier to read your code and understand what data is being used, 
especially when compared to the numbered indexes you used in the prior exercise.

Your job in this exercise is to create a dictionary directly from the data file using DictReader. 
NOTE: The misspellings are from the original data, and this is a very common issue. 
Again, the baby_names dictionary has already been created for you
"""

# Import the python CSV module
import csv

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('baby_names.csv','r')

# Loop over a DictReader on the file
for row in csv.DictReader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row['NAME']

# Print the dictionary keys
print(baby_names.keys())