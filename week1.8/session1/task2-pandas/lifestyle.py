import pandas

data = pandas.read_csv("C:/Users/oufta/Desktop/Repos/COMP1850-Semester1/week1.8/session1/task2-pandas/lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
lenData = len(data)
print(lenData)

# Find the mean average GPA of the students

print(data["GPA"].sum() / lenData)

# Find the standard deviation of how much sleep students get per day

print(data["Sleep_Hours_Per_Day"].std())

# Find the maximum amount of study hours per day

print(data["Study_Hours_Per_Day"].max())

# Sort the students by social hours per day ascending (lowest -> highest)

sortedData = data.sort_values("Social_Hours_Per_Day")

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

extraData = data.copy()
extraData["Total_hours"] = data["Study_Hours_Per_Day"] + data["Sleep_Hours_Per_Day"] + data["Social_Hours_Per_Day"] + data["Extracurricular_Hours_Per_Day"] + data["Physical_Activity_Hours_Per_Day"]

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?

highStressData = data[data["Stress_Level"] == "High"]
lowStressData = data[data["Stress_Level"] == "Low"]

print(highStressData["GPA"].mean())
print(lowStressData["GPA"].mean())

# As demonstrated by the print statements above, high stress is correlated to a higher GPA.