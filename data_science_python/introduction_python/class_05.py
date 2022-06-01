"""
Replace list elements
Replacing list elements is pretty easy. Simply subset the list and assign new values to the subset. 
You can select single elements or you can change entire list slices at once.

Use the IPython Shell to experiment with the commands below. Can you tell what's happening and why?

x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
For this and the following exercises, you'll continue working on the areas list that 
contains the names and areas of different rooms in a house.
"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[5] = "chill zone"


"""
Extend a list
If you can change elements in a list, you sure want to be able to add elements to it, right? 
You can use the + operator:

x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
You just won the lottery, awesome! You decide to build a poolhouse and a garage. 
Can you add the information to the areas list?
"""

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage",15.45]



"""
Inner workings of lists
At the end of the video, Hugo explained how Python lists work behind the scenes. 
In this exercise you'll get some hands-on experience with this.

The Python code in the script already creates a list with the name areas and a copy named areas_copy. 
Next, the first element in the areas_copy list is changed and the areas list is printed out. 
If you hit Run Code you'll see that, although you've changed areas_copy, 
the change also takes effect in the areas list. That's because areas and areas_copy point to the same list.

If you want to prevent changes in areas_copy from also taking effect in areas, 
you'll have to do a more explicit copy of the areas list. You can do this with list() or by using [:].
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)