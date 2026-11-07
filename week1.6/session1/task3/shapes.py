# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle(Shape):

    def __init__(self, radius, center, colour = "red"):
        """ Constructs a Circle using the radius, center and colour (default: red) provided. """
        super().__init__(center, colour)
        self.set_radius(radius)

    def set_radius(self, radius):
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError("Inappropriate radius data type!")

        if radius <= 0:
            raise ValueError("Radius must be greater than 0!")

        self.radius = radius

    def __str__(self):
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    
    def area(self):
        """ Returns the area of this circle. """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """ Returns the circumference of this circle. """
        return math.pi * 2 * self.radius