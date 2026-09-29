"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mohamad Ftayeh
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")


# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

monthlySavings = input("How much would you like to save this month?: ")

if (not monthlySavings.isnumeric()):
    print("Invalid value!")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
else:
    MONTHS_PER_YEAR = 12
    yearlySavings = float(monthlySavings) * MONTHS_PER_YEAR
    print("Your savings for the year would be", yearlySavings)


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

    INTEREST_MULTIPLIER = 0.008
    interest = yearlySavings * INTEREST_MULTIPLIER
    finalSavings = yearlySavings + interest
    finalSavingsFormatted = f"£{finalSavings:.2f}"
    print("Your final savings for this year would be", finalSavingsFormatted, "with interest.")