"""
Adding and extending dictionaries
If you have a dictionary and you want to add data to it, 
you can simply create a new key and assign the data you desire to it. 
It's important to remember that if it's a nested dictionary, 
then all the keys in the data path must exist, and each key in the path must be assigned individually.

You can also use the .update() method to update a dictionary with keys and values from another dictionary, 
tuples or keyword arguments.

Here, you'll combine several techniques used in prior exercises to setup 
your dictionary in a way that makes it easy to find the least popular baby name for each year.

Your job is to add data for the year 2011 to your dictionary by assignment, 
2012 by update, and then find the least popular baby name for each year.
"""

# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1,'Casey'), (2,'Aiden')])

# Loop over the years in the boy_names dictionary 
for year in boy_names:
    # sort the data for each year by descending rank and get the lowest one
    lowest_ranked = sorted(boy_names[year], reverse=True)[0]
    # Safely print the year and the least popular name or 'Not Available'
    print(year, boy_names[year].get(lowest_ranked, 'Not Available'))


"""
Popping and deleting from dictionaries
Often, you will want to remove keys and value from a dictionary. 
You can do so using the del Python instruction. 
It's important to remember that del will throw a KeyError if the key you are trying to delete does not exist. 
You can not use it with the .get() method to safely delete items; however, it can be used with try: catch:.

If you want to save that deleted data into another variable for further processing, 
the .pop() dictionary method will do just that. 
You can supply a default value for .pop() much like you did for .get() to safely deal with missing keys.
It's also typical to use .pop() instead of del since it is a safe method.

Here, you'll remove 2011 and 2015 to save them for later, and then delete 2012 from the dictionary.
"""


# Remove 2011 from female_names and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 from female_names with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015,{})

# Delete 2012 from female_names
del female_names[2012]

# Print female_names
print(female_names)