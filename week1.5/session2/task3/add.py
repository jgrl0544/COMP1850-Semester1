# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum

import money

onePound = money.Money(1, 0)
print(onePound)
ninetyNinePence = money.Money(0, 99)
print(ninetyNinePence)
twoPence = money.Money(0, 2)

onePoundNinetyNine = onePound.__add__(ninetyNinePence)

print(onePoundNinetyNine)
twoPoundsAndOnePence = onePoundNinetyNine.__add__(twoPence)
print(twoPoundsAndOnePence)


# The following lines of code have been commented out as they cause errors.

# incorrectDataType = money.Money("one pound", "ten trillion pence")
# incorrectNumber = money.Money(100, 100)
# incorrectNumberAlso = money.Money(-50, 50)