
def func_1(lst_value): 
    ''' 
    This function returns the mean of the digits that make up 1st_value. 
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 