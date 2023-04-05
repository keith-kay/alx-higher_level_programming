#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 3-rectangle.py)"""


class Rectangle:
    """Represent a rectangle and its arguments"""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.
        Args:
            width (int): The horizontal dimension of the rectangle.
            height (int): The vertical dimension of the rectangle.
        """
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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the vertical dimension of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rctngl = []
        for i in range(self.__height):
            [rctngl.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rctngl.append("\n")
        return ("".join(rctngl))

    def __repr__(self):
        rctngl = "Rectangle(" + str(self.__width)
        rctngl += ", " + str(self.__height) + ")"
        return (rctngl)
