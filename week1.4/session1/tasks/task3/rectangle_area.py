
# function implementation

def rectangle_area(length, width):  # define suitable input data
    return length * width              # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(5, 10)}")   # provide suitable data matching your inputs

def EvenNumbersUntil(end):
    for index in range(0, end+1):
        if (index % 2 == 0): print(index)