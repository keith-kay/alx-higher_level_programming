#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 6-rectangle.py)"""


class Rectangle:
    """Represent a rectangle and its arguments.
    Args:
        instances (int): The number of Rectangle instances.
        output(any): The symbol used for string representation.
    """

    instances = 0
    output = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle.
        Args:
            width (int): The horizontal dimension of the rectangle.
            height (int): The vertical dimension of the rectangle.
        """
        type(self).instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the horizontal dimension of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Get the horizontal dimension of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    def area(self):
        """Return the rectangle’s area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the rectangle’s perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rctngl = []
        for i in range(self.__height):
            [rctngl.append(str(self.output)) for j in range(self.__width)]
            if i != self.__height - 1:
                rctngl.append("\n")
        return ("".join(rctngl))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rctngl = "Rectangle(" + str(self.__width)
        rctngl += ", " + str(self.__height) + ")"
        return (rctngl)

    def __del__(self):
        """Output rectangle’s deletion message."""
        type(self).instances -= 1
        print("Closing rectangle")
