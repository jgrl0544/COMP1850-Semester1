# Worksheet 1.2: Task 2 Solution

from util import read_numbers
import sys

def getMean(list):
      return sum(list) / len(list)

def getMedian(list):
    list = sorted(list) 
    listLength = len(list)

    if (listLength % 2 == 1): # if odd
        index = round(listLength / 2) - 1 # -1 because 0-based list
        return list[index]
    
    else: 
        smallerIndex = round(listLength / 2) - 1
        largerIndex = round(listLength / 2)
        total = list[smallerIndex] + list[largerIndex]
        return total / 2


print("Welcome to the \"various statistics about a list\" program!")
numberList = read_numbers()

if (len(numberList) == 0):
    sys.exit("Error: no numbers provided")
    
print(f"Minimum = {min(numberList)}")
print(f"Maximum = {max(numberList)}")
print(f"Mean = {getMean(numberList)}")
print(f"Median = {getMedian(numberList)}")