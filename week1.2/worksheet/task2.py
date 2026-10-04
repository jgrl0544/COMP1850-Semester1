# Worksheet 1.2: Task 2 Solution

from util import read_numbers
import sys

def getMean(floatList):
      return sum(floatList) / len(floatList)

def getMedian(floatList):
    floatList = sorted(floatList) 
    listLength = len(floatList)

    if (listLength % 2 == 1): # if odd
        index = round(listLength / 2) - 1 # -1 because 0-based list
        return floatList[index]
    
    else: 
        smallerIndex = round(listLength / 2) - 1
        largerIndex = round(listLength / 2)
        total = floatList[smallerIndex] + floatList[largerIndex]
        return total / 2


print("Welcome to the \"various statistics about a list\" program!")
floatsList = read_numbers()

if (len(floatsList) == 0):
    sys.exit("Error: no numbers provided")
    
print(f"Minimum = {min(floatsList)}")
print(f"Maximum = {max(floatsList)}")
print(f"Mean = {getMean(floatsList)}")
print(f"Median = {getMedian(floatsList)}")