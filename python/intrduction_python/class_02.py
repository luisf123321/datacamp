# functions



"""
Load a DataFrame
A ransom note was left at the scene of Bayes' kidnapping. Eventually, 
we'll want to analyze the frequency with which each letter occurs in the note, 
to help us identify the kidnapper. For now, we just need to load the data from ransom.csv into Python.

We'll load the data into a DataFrame, a special data type from the pandas module. 
It represents spreadsheet-like data (something with rows and columns).

We can create a DataFrame from a CSV (comma-separated value) file by using the function pd.read_csv()

"""

# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)


"""
Correcting a function error
The code in the script editor should plot information from the DataFrame that we loaded in the previous exercise.

However, there is an error in function syntax. Remember that common function errors include:

Forgetting closing parenthesis
Forgetting commas between each argument

Note that all arguments to the functions are correct. The problem is in the function syntax.

"""
# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors

# Plot a graph
#plt.plot(x_values , y_values)

# Display the graph
#plt.show()


"""

We need to narrow down the list of suspects for the kidnapping of Bayes. 
Once we have a list of suspects, we'll ask them for writing samples and compare them to the ransom note.

A witness to the crime noticed a green truck leaving 
the scene of the crime whose license plate began with 'FRQ'. 
We'll use this information to search for some suspects.

As a detective, you have access to a special function called lookup_plate.

lookup_plate accepts one positional argument: A string representing a license plate.

"""

# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = ('FRQ****')
lookup_plate(plate)


"""
We need to narrow down the list of suspects for the kidnapping of Bayes. 
Once we have a list of suspects, we'll ask them for writing samples and compare them to the ransom note.

A witness to the crime noticed a green truck leaving the scene of 
the crime whose license plate began with 'FRQ'. We'll use this information to search for some suspects.

As a detective, you have access to a special function called lookup_plate.

lookup_plate accepts one positional argument: A string representing a license plate.
"""


# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color='Green')