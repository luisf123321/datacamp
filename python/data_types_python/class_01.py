
"""
Manipulating lists for fun and profit
You may be familiar with adding individual data elements to a list by using the .append() method. 
However, if you want to combine a list with another array type (list, set, tuple), 
you can use the .extend() method on the list.

You can also use the .index() method to find the position of an item in a list. 
You can then use that position to remove the item with the .pop() method.

In this exercise, you'll practice using all these methods!
"""

# Create a list containing the names: baby_names
baby_names = ['Ximena','Aliza','Ayden','Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(['Rowen','Sandeep'])

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index('Aliza')

# Remove 'Aliza' from baby_names
baby_names.pop(1)

# Print baby_names
print(baby_names)



"""
Looping over lists
You can use a for loop to iterate through all the items in a list. 
You can take that a step further with the sorted() function which will sort the data in a 
list from lowest to highest in the case of numbers and alphabetical order if the list contains strings. 
You can learn more about for in this DataCamp Tutorial.

The sorted() function returns a new list and does not affect the list you passed into the function. 
You can learn more about sorted() in the Python documentation.

A list of lists, records has been pre-loaded. 
If you explore it in the IPython Shell, you'll see that each entry is a list of this form:

['2011', 'FEMALE', 'HISPANIC', 'GERALDINE', '13', '75']

The name of the baby ('GERALDINE') is the fourth entry of this list. 
Your job in this exercise is to loop over this list of lists and append the names of each 
baby to a new list called baby_names.
"""


# Create the empty list: baby_names
baby_names = []

# Loop over records 
for row in records:
    # Add the name to the list
    baby_names.append(row[3])
    
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)