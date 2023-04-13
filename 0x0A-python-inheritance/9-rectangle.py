#!/usr/bin/python3
# 9-rectangle.py

"""Class basegeometry module"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
    """

    def __init__(self, width, height):
        """Initilize rectangle function"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """function that returns area of rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns a string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
