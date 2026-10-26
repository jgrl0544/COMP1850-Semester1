
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Mohamad Ftayeh
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    new_amount = amount * conversion_rate[from_currency][to_currency] # gets the value from the dictionary
    new_amount = round(new_amount, 2) # rounds it as needed.
    new_amount = max(0, new_amount) # assigns 0 if it's the larger of the two numbers (new_amount is negative)
    
    return new_amount # the return value