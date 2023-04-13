#!/usr/bin/python3
# 7-base_geometry.py


class BaseGeometry:
    """BaseGeometry class"""

    @abstractmethod
    def area(self) -> float:
        """abstract method for calculating area"""

    def integer_validator(self, name: str, value: int) -> None:
        """Method for validating if a number is an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
