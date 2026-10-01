# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}") # replaces the string with lowercase letters
print(f"Modified String 2: {user_string.upper()}") # replaces the string with uppercase letters
print(f"Modified String 3: {user_string.strip()}") # strips a string of trailing and ending whitespaces.
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces all instances of the character a with @
print(f"Modified String 5: {user_string.capitalize()}") # capitalizes the first character of the string, if it can be capitalized.
print(f"Modified String 6: {user_string[::-1]}") # returns the array, such that it is stepped backwards, meaning it returns the string but reversed.
print(f"Modified String 7: {user_string.title()}") # returns the string where every word is capitalized (see .capitalize()).
print(f"Modified String 8: {len(user_string)}") # returns the length of the character array, without the null terminator
print(f"Modified String 9: {user_string.find('a')}") # returns the first index where the letter a is found.
print(f"Modified String 10: {user_string.count('a')}") # returns the number of items the letter a is found.
print(f"Modified String 11: {user_string.startswith('Hello')}") # checks if the string starts with Hello.
print(f"Modified String 12: {user_string.endswith('!')}") # checks if the string ends with an exclaamtion mark.
print(f"Modified String 13: {user_string.isalnum()}") # checks if the string is made up of strictly alphanumeric characters.
print(f"Modified String 14: {user_string.isalpha()}") # checks if the string is made up of strictly alphabetical characters.
print(f"Modified String 15: {user_string.isdigit()}") # checks if the string is made up of strictly numerical characters.


######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!