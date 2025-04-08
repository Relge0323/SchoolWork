"""
File: piechart.py

Displays a pie chart of monthly living expenses.
"""

import matplotlib.pyplot as plt

# Prepare the data
expenses = {"Rent":1200, "Food":700, "Healthcare":500, "Transportation":300, "Utilities":600, "Entertainment":200}
labels = list(expenses.keys())
slices = list(expenses.values())

# Set up and show the pie chart
plt.pie(slices, labels = labels, autopct = "%1.1f%%")
plt.title("Pie Chart of Living Expenses")
plt.show()