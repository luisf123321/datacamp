"""
Finding all the data and the overlapping data between sets
Sets have several methods to combine, compare, and study them all based on mathematical set theory. 
The .union() method returns a set of all the names found in the set you used the method 
on plus any sets passed as arguments to the method. 
You can also look for overlapping data in sets by using the .intersection() method on a set and 
passing another set as an argument. It will return an empty set if nothing matches.

Your job in this exercise is to find the union and intersection in the names from 2011 and 2014. 
For this purpose, two sets have been pre-loaded into your workspace: baby_names_2011 and baby_names_2014.

One quirk in the baby names dataset is that names in 2011 and 2012 are all in upper case, 
while names in 2013 and 2014 are in title case (where the first letter of each name is capitalized). 
Consequently, if you were to compare the 2011 and 2014 data in this form, 
you would find no overlapping names between the two years! To remedy this, 
we converted the names in 2011 to title case using Python's .title() method.

Real-world data can often come with quirks like this - it's important to catch them to ensure your 
results are meaningful.

"""

# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))


"""
Determining set differences
Another way of comparing sets is to use the difference() method. It returns all the items found 
in one set but not another. It's important to remember the set you call the method on will be the one 
from which the items are returned. Unlike tuples, you can add() items to a set. 
A set will only add items that do not exist in the set.

In this exercise, you'll explore what names were common in 2011, but are no longer common in 2014. 
The set baby_names_2014 has been pre-loaded into your workspace. As in the previous exercise, 
the names have been converted to title case to ensure a proper comparison.
"""

# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0] == '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)