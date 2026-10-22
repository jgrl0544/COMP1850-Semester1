# Week 4, Session 2: Task 4

# Given an incomplete recursive function power to calculate x raised to
# the power of n, your task is to complete the function.


def power(x, n, rt = 1):
    print(rt)
    if (n == 0): 
        return rt

    rt = rt * x
    return power(x, n-1, rt)

# Once completed, make at least two function calls to test the power function
print(power(5,2))