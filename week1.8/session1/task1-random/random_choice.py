import random

# Read names from a file

with open("C:/Users/oufta/Desktop/Repos/COMP1850-Semester1/week1.8/session1/task1-random/names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line

count = int(input("How many random names would you like to pull?: "))

newNames = []
for _ in range(count):
    while (True):
        if (len(names) == len(newNames)): break # in case names are exhausted.
        name = names[random.randint(0, len(names)-1)]
        if name not in newNames:
            newNames.append(name)
            break

for index in newNames:
    print(index)