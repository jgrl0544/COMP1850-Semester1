num1Str = input("Please enter an integer value for 1: ")
num2Str = input("Please enter an integer value for 2: ")


if (num1Str.strip("-").isnumeric() and num2Str.strip("-").isnumeric()):

    num1 = float(num1Str)
    num2 = float(num2Str)

    if (num1.is_integer() and num2.is_integer()):
         result = num1 * num2
         print(f"The result is {result}")
    else:
         print("That is not an integer")
    
else:
     print ("That is not a number")