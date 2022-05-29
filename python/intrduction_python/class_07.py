#matplotlib

"""
Adding a legend
Officers Deshaun, Mengfei, and Aditya have all been working with you to solve the kidnapping of Bayes. 
Their supervisor wants to know how much time each officer has spent working on the case.

Deshaun created a plot of data from the DataFrames deshaun, mengfei, and aditya in the previous exercise. 
Now he wants to add a legend to distinguish the three lines.
"""



"""
Adding labels
If we give a chart with no labels to Officer Deshaun's supervisor, she won't know what the lines represent.

We need to add labels to Officer Deshaun's plot of hours worked.
"""
# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title("time")

# Add y-axis label
plt.ylabel("hour")

# Legend
plt.legend()
# Display plot
plt.show()


"""

Adding floating text
Officer Deshaun is examining the number of hours that he worked over the past six months. 
The number for June is low because he only had data for the first week. 
Help Deshaun add an annotation to the graph to explain this.
"""


# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5,80,"Missing June data")

# Display graph
plt.show()