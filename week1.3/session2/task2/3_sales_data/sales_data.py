# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows

import csv 



with open('/workspaces/COMP1850-Semester1/week1.3/session2/task2/3_sales_data/sales.csv', mode='r', encoding='utf-8') as handle:
    reader = csv.reader(handle)
    next(reader)
    widgets = {"" : 0}
    totalSales = 0
    rows = 0
    for line in reader:
        rows += 1
        totalSales += int(line[3])
        print(f"ON {line[0]} WE SOLD {line[3]} OF {line[1]} AT {line[4]}")
        widgets[line[1]] = int(widgets.get(line[1], 0)) + int(line[3])

    print(f"Average is {totalSales / rows:.02f}")

    maxKey = ""
    maxVal = 0
    for k, v in widgets.items():
         if v > maxVal:
            maxKey = k
            maxVal = v
    
    print(f"Highest sales is from {maxKey} with {maxVal}")