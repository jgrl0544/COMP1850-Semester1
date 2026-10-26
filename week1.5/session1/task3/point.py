# Week 1.5, Session 1: Task 3

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

# Finally, add code here to demonstrate use of Point

point = Point(0,0)
otherPoint = Point(5,6)

print(point.distance())
print(point.distanceTo(otherPoint))