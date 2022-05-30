"""
Creating and looping through dictionaries
You'll often encounter the need to loop over some array type data, like in Chapter 1, 
and provide it some structure so you can find the data you desire quickly.

You start that by creating an empty dictionary and assigning part of your array data as 
the key and the rest as the value.

Previously, you used sorted() to organize your data in a list. 
Dictionaries can also be sorted. By default, using sorted() on a dictionary will sort 
by the keys of the dictionary. You can also reverse the order by passing reverse=True as a keyword argument.

Finally, since sorted returns a list, you can use slice notation to select only part of the list. 
For example, [:10] will slice the first ten items off a list and return only those items.
"""


# Create an empty dictionary: names_by_rank
names_by_rank = {}

# Loop over the girl names
for rank, name in female_baby_names_2012.items():
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name
    
# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for rank in sorted(names_by_rank, reverse=True)[:10]:
    # Print each item
    print(names_by_rank[rank])

"""
Safely finding by key
As demonstrated in the video, if you attempt to access a key that isn't present in a dictionary, 
you'll get a KeyError. One option to handle this type of error is to use a try: except: block. 
You can learn more about error handling in Python Data Science Toolbox (Part 1), specifically in this video.

Python provides a faster, more versatile tool to help with this problem in the form of the .get() method.
The .get() method allows you to supply the name of a key, and optionally, 
what you'd like to have returned if the key is not found.

You'll be using same names dictionary from the previous exercise and will gain practice using the .get() method.
"""

# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))


# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.get(105,'Not Found'))

"""
Dealing with nested data
A dictionary can contain another dictionary as the value of a key, 
and this is a very common way to deal with repeating data structures such as yearly, 
monthly or weekly data. All the same rules apply when creating or accessing the dictionary.

For example, if you had a dictionary that had a ranking of my cookie consumption by year and type of cookie. 
It might look like 
cookies = {'2017': {'chocolate chip': 483, 'peanut butter': 115}, 
    '2016': {'chocolate chip': 9513, 'peanut butter': 6792}}. 
I could access how many chocolate chip cookies I ate in 2016 using cookies['2016']['chocolate chip'].

When exploring a new dictionary, it can be helpful to use the .keys() method to get an 
idea of what data might be available within the dictionary. 
You can also iterate over a dictionary and it will return each key in the dictionary 
for you to use inside the loop. Here, a dictionary called boy_names has been loaded into your workspace. 
It consists of all male names in 2013 and 2014.
"""

# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, 'Unknown'))