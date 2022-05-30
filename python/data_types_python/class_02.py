#tuples

"""
Tuples are made of several items just like a list, but they cannot be modified in any way. 
It is very common for tuples to be used to represent data from a database. 
If you have a tuple like ('chocolate chip cookies', 15) and you want to access each part of the data,
 you can use an index just like a list. However, you can also "unpack" the tuple into multiple variables 
 such as type, count = ('chocolate chip cookies', 15) that will set type to 'chocolate chip cookies' and 
 count to 15.

Often you'll want to pair up multiple array data types. The zip() function does just that. 
It will return a list of tuples containing one element from each list passed into zip().

When looping over a list, you can also track your position in the list by using the enumerate() function. 
The function returns the index of the list item you are currently on in the list and the list item itself.

You'll practice using the enumerate() and zip() functions in this exercise, 
in which your job is to pair up the most common boy and girl names. 
Two lists - girl_names and boy_names - have been pre-loaded into your workspace.
"""


# Pair up the girl and boy names: pairs
pairs = list(zip(girl_names,boy_names))

# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))


"""
Making tuples by accident
Tuples are very powerful and useful, and it's super easy to make one by accident. 
All you have to do is create a variable and follow the assignment with a comma. 
This becomes an error when you try to use the variable later expecting it to be a string or a number.

You can verify the data type of a variable with the type() function. In this exercise, 
you'll see for yourself how easy it is to make a tuple by accident.
"""


# Create the normal variable: normal
normal = 'simple'

# Create the mistaken variable: error
error = 'trailing comma',

# Print the types of the variables
print(type(normal))
print(type(error))