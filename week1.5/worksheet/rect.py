# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if (not (isinstance(width, int) and isinstance(height, int))):
            raise TypeError("Only ints can be used for height and width.")
        elif (not (width > 0 and height > 0)):
            raise ValueError("The width/height provided is not suitable.")

        self.width = width
        self.height = height

    def is_square(self):
        """ Returns whether the width and height represent the same value. """
        return self.width == self.height

    def area(self):
        """ Returns the area of the rectangle. """
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of the rectangle. """
        return 2 * (self.width + self.height)
