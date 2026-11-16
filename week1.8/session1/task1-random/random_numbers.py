import random

# Get user to input how many random numbers they want
count = int(input("How many random numbers would you like?: "))

with open("C:/Users/oufta/Desktop/Repos/COMP1850-Semester1/week1.8/session1/task1-random/random.txt", "w") as file:

# Generate this many random numbers
    for index in range(count):
        number = random.random()

# Write the random numbers to a file named random.txt, one number per line
        file.write(str(number) + "\n")


