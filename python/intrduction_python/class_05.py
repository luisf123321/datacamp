#pandas

"""
Logical testing
Let's practice writing logical statements and displaying the output.

Recall that we use the following operators:

== tests that two values are equal.
!= tests that two values are not equal.
> and < test that greater than or less than, respectively.
>= and <= test greater than or equal to or less than or equal to, respectively.

"""
# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

# Is fur_color not equal to "brown"?
print(fur_color != "brown")


"""
Selecting missing puppies
Let's return to our DataFrame of missing puppies, which is loaded as mpr. 
Let's select a few different rows to learn more about the other missing dogs.
"""

# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == "Still Missing"]
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr["Dog Breed"] != "Poodle"]
print(not_poodle)

"""
Narrowing the list of suspects
In Chapter 1, we found a list of people whose cars matched the description of the one that kidnapped Bayes:

Fred Frequentist
Ronald Aylmer Fisher
Gertrude Cox
Kirstine Smith
We'd like to narrow this list down, so we obtained credit card records for each suspect. 
We'd like to know if any of them recently purchased dog treats to use in the kidnapping. 
If they did, they would have visited 'Pet Paradise'.

The credit records have been loaded into a DataFrame called credit_records.
"""