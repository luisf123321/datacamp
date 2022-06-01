#list


"""
Create a list
As opposed to int, bool etc., a list is a compound data type; you can group values together:

a = "is"
b = "nice"
my_list = ["my", "list", a, b]

After measuring the height of your family, you decide to collect some 
information on the house you're living in. 
The areas of the different parts of your house are stored in separate variables for now, 
as shown in the script.
"""

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall,kit,liv,bed,bath]

# Print areas
print(areas)

"""
Create list with different types
A list can contain any Python type. Although it's not really common, 
a list can also contain a mix of Python types including strings, floats, booleans, etc.

The printout of the previous exercise wasn't really satisfying. 
It's just a list of numbers representing the areas, 
but you can't tell which area corresponds to which part of your house.

The code in the editor is the start of a solution. For some of the areas, 
the name of the corresponding room is already placed in front. Pay attention here! "bathroom" is a string, 
while bath is a variable that represents the float 9.50 you specified earlier.
"""

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [ "hallway",hall,"kitchen", kit, "living room", liv,"bedroom", bed, "bathroom", bath]

# Print areas
print(areas)


"""
List of lists
As a data scientist, you'll often be dealing with a lot of data, 
and it will make sense to group some of this data.

Instead of creating a flat list containing strings and floats, 
representing the names and areas of the rooms in your house, you can create a list of lists. 
The script in the editor can already give you an idea.

Don't get confused here: "hallway" is a string, 
while hall is a variable that represents the float 11.25 you specified earlier.
"""

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom",bed],
         ["bathroom",bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))