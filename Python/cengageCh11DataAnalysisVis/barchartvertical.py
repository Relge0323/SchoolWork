"""
File: barchartvertical.py

Displays enrollments in three courses
in a vertical bar chart.
"""

import matplotlib.pyplot as plt
 
# Prepare the data
data = {"CSCI112":40, "CSCI312":32, "PHIL258":19}
courses = list(data.keys())
enrollments = list(data.values())
colors = ['purple', 'orange', 'green']

# Set up and show the vertical bar chart
plt.figure(figsize = (4,4))
plt.bar(courses, enrollments, width = 0.2, color=colors)
plt.title("Students Enrolled in Ken's Courses")
plt.xlabel("Course")
plt.ylabel("Number of students")
plt.show()



