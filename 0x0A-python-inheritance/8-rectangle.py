#!/bin/usr/python3
# 8-rectangle.py

"""Rectangle class module"""

class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
