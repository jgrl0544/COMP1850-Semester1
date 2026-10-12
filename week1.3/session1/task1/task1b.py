# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# fruit.pop() pops an item from the list while also returning it.
# therefore, eventually, fruit does not return true (i.e. it is eventually empty)

# What features of Python does it rely on?
# It relies on pythons list datatype and the way it is cast to bool.