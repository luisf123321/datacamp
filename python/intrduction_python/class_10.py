#matplotlib

"""
Build a simple bar chart
Officer Deshaun wants to plot the average number of hours worked per week for him and his coworkers. 
He has stored the hours worked in a DataFrame called hours, 
which has columns officer and avg_hours_worked. Recall that the function plt.bar() takes two arguments: 
the labels for each bar, and the height of each bar. Both of these can be found in our DataFrame.
"""

# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
plt.bar(hours.officer, hours.avg_hours_worked,
        # Add error bars
        yerr=hours.std_hours_worked)

# Display the plot
plt.show()


"""
Where did the time go?
Officer Deshaun wants to compare the hours spent on field work and desk work between him and his colleagues. 
In this DataFrame, he has split out the average hours worked per week into desk_work and field_work.

You can use the same DataFrame containing the hours worked from the previous exercise (hours).
"""

# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label='Desk Work')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer, hours.field_work, bottom=hours.desk_work)

# Add a legend
plt.legend()

# Display the plot
plt.show()
# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label='Desk Work')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer, hours.field_work, bottom=hours.desk_work, label= 'Field Work')

# Add a legend
plt.legend()

# Display the plot
plt.show()