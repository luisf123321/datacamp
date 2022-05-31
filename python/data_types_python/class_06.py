"""
Working with dictionaries more pythonically
So far, you've worked a lot with the keys of a dictionary to access data, 
but in Python, the preferred manner for iterating over items in a dictionary is with the .items() method.

This returns each key and value from the dictionary as a tuple, which you can unpack in a for loop. 
You'll now get practice doing this.
"""

# Iterate over the 2014 nested dictionary
for rank, name in baby_names[2014].items():
    # Print rank and name
    print(rank, name)
    
# Iterate over the 2012 nested dictionary
for rank, name in baby_names[2012].items():
    # Print rank and name
    print(rank, name)
  
"""
Checking dictionaries for data
You can check to see if a key exists in a dictionary by using the in expression.

For example, you can check to see if 'cookies' is a key in the dictionary 
by using if 'cookies' in recipes_dict: this allows you to safely react to data being present in the dictionary.

You can also use the in expression so see if data is in the value of a dictionary such as if 'cookies' in 
recipes_dict.values(). Remember you have to handle nested dictionaries differently as illustrated 
in the video and previous exercises, and use the in expression on each nested dictionary.
"""

# Check to see if 2011 is in baby_names
if 2011 in baby_names:
    # Print 'Found 2011'
    print('Found 2011')
    
# Check to see if rank 1 is in 2012
if 1 in baby_names[2012]:
    # Print 'Found Rank 1 in 2012' if found
    print('Found Rank 1 in 2012')
else:
    # Print 'Rank 1 missing from 2012' if not found
    print('Rank 1 missing from 2012')
    
# Check to see if Rank 5 is in 2013
if 5 in baby_names[2013]:
   # Print 'Found Rank 5'
   print('Found Rank 5')