# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

import math
class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.hypot(self.x, self.y)

    def distanceTo(self, other):
        diffX = other.x - self.x
        diffY = other.y - self.y
        return math.hypot(diffX, diffY)

class Circle:
    """
    A circle, defined by a radius and a centre point.
    """

    def __init__(self, rad, centre = Point(0,0)):
        self.rad = rad
        self.centre = centre

    def area(self):
        return math.pi * self.rad * self.rad

    def perimeter(self):
        return 2 * math.pi * self.rad