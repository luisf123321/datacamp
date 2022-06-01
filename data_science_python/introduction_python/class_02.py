#Variables

"""
Variable Assignment
In Python, a variable allows you to refer to a value with a name. To create a variable use =, like this example:

x = 5
You can now use the name of this variable, x, instead of the actual value, 5.

Remember, = in Python means assignment, it doesn't test equality!
"""

# Create a variable savings
savings = 100

# Print out savings
print(savings)


"""
Calculations with variables
Remember how you calculated the money you ended up with after 7 years of investing $100? 
You did something like this:

100 * 1.1 ** 7
Instead of calculating with the actual values, you can use variables instead. 
The savings variable you've created in the previous exercise represents the $100 you started with. 
It's up to you to create a new variable to represent 1.1 and then redo the calculations!
"""

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings *  growth_multiplier ** 7

# Print out result
print(result)

"""
Other variable types
In the previous exercise, you worked with two Python data types:

int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
float, or floating point: a number that has both an integer and fractional part, separated by a point. growth_multiplier, with the value 1.1, is an example of a float.
Next to numerical data types, there are two other very common data types:

str, or string: a type to represent text. You can use single or double quotes to build a string.
bool, or boolean: a type to represent logical values. Can only be True or False (the capitalization is important!).
"""

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True


"""
Guess the type
To find out the type of a value or a variable that refers to that value, you can use the type() function. 
Suppose you've defined a variable a, but you forgot the type of this variable. 
To determine the type of a, simply execute:

type(a)
We already went ahead and created three variables: a, b and c. 
You can use the IPython shell to discover their type. Which of the following options is correct?
"""


"""
Operations with other types
Hugo mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.
"""

savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of savings and growth_multiplier to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc 

# Print out doubledesc
print(doubledesc)


"""
Type conversion
Using the + operator to paste together two strings can be very useful in building custom messages.

Suppose, for example, that you've calculated the return of your investment and want to 
summarize the results in a string. Assuming the integer savings and float result are defined, 
you can try something like this:

print("I started with $" + savings + " and now have $" + result + ". Awesome!")
This will not work, though, as you cannot simply sum strings and integers/floats.

To fix the error, you'll need to explicitly convert the types of your variables. 
More specifically, you'll need str(), to convert a value into a string. str(savings), 
for example, will convert the integer savings to a string.

Similar functions such as int(), float() and bool() will help you convert Python values into any type.
"""

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)