# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables) # prints tomato as both are taken to be sets due to the curly brackets
print(both)

# Why does the following code diplay five items?

food = fruit.union(vegetables) 
print(food)
# unions are similar to OR statements, so it just prints everything printed within either of the two. 
# tomatoes are not repeated because they exist as one instance in the intersection. 

# Add an item to fruit
fruit.add("pear")

# Remove an item from vegetables
vegetables.pop()

# Find and display symmetric difference of the two sets
# disjunctive union, i.e. XOR

symDiffAlso = fruit.symmetric_difference(vegetables)
print(symDiffAlso)

#symDiff = fruit.union(vegetables).discard(fruit.intersection(vegetables))
#print(symDiff)