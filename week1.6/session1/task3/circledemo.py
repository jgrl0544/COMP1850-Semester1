# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from point import Point
from shapes import Circle

circle = Circle(5, Point(0,0))

print(circle)

print(circle.area())

circle.set_position(Point(0,1))

print(circle)

circle.set_colour("green")

print(circle)