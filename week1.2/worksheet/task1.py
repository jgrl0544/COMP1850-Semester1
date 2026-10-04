# Worksheet 1.2: Task 1 Solution
import sys

HIGH_PASS = "Distinction"
LOW_PASS = "Pass"
FAIL = "Fail"

print("Welcome!")
print("Grades are as follows: \n0-39 is a fail. \n40-69 is a pass. \n70-100 is a pass with distinction.")

userInput = input("Please enter a grade: ")
# ORs are evaluated left-to-right, so it's safe to cast userInput to int on the second condition. 
if not (userInput.isdecimal() and (0 <= int(userInput) <= 100)): 
    sys.exit("Error: Grade must be an integer between 0 and 100")

score = int(userInput)
message = ""

if (score >= 70): 
    message = HIGH_PASS
elif (score >= 40): 
    message = LOW_PASS
else: 
    message = FAIL

print(f"{score} is a {message}")