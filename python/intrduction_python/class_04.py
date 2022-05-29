#pandas


"""
Two methods for selecting columns
Once again, we've loaded the credit card records of our four suspects into a DataFrame called credit_records. 
Let's examine the items that they've purchased.

The pandas module has been imported under the alias pd. 
The DataFrame credit_records has already been imported.
"""

# Select the column item from credit_records
# Use dot notation
items = credit_records.item

# Display the results
print(items)


"""
Correcting column selection errors
A junior detective tried to access the location columns of credit_records, but he made some mistakes. 
Help correct his code so that we can search for suspicious purchases.

In all exercises going forward, pandas will be imported as pd. 
The DataFrame credit_records has already been imported.
"""
# One or more lines of code contain errors.
# Fix the errors so that the code runs.

# Select the location column in credit_records
location = credit_records['location']

# Select the item column in credit_records
items = credit_records.item

# Display results
print(location)


"""
More column selection mistakes
Another junior detective is examining a DataFrame of Missing Puppy Reports. 
He's made some mistakes that cause the code to fail.

The pandas module has been loaded under the alias pd, and the DataFrame is called mpr.
"""


# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr["Dog Name"]

# Select column "Missing?" from mpr
is_missing = mpr["Missing?"]

# Display the columns
print(name)
print(is_missing)