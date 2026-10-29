# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

import data

exampleData = data.Dataset("/workspaces/COMP1850-Semester1/week1.5/session2/task5/exampleData.txt")
print(len(exampleData))
print(exampleData.mean())
print(exampleData.median())