# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

with open("/workspaces/COMP1850-Semester1/week1.3/session2/task3/1_user_info/user_info.txt", "a") as handle:
    while True:
        if (input("Input 0 to save and exit program, anything else to continue: ") == "0"): break
        name = input("Name: ")
        age = input("Age: ")
        color = input("Fav Color: ")
        handle.write(f"{name}, {age}, {color}\n")




# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
