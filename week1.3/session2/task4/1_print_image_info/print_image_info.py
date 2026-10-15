# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)

fileName = input("Enter file name: ")
try: 
    with open("/workspaces/COMP1850-Semester1/week1.3/session2/task4/images/" + fileName, "r") as handle:
        handle.readline() # ignore the magic number.
        dimensions = handle.readline().split()
        maxGrayValue = int(handle.readline())
        print(f"The dimensions of {fileName} are X = {dimensions[0]} and Y = {dimensions[1]} and the max grey val is {maxGrayValue}.")
except FileNotFoundError:
    print("This file does not exist.")