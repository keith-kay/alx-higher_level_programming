#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a function a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the division.
    """

    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    # define error message string
    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)
    # check if matrix is a list of lists and raise a TypeError
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)
    # check if matrix is an integer or a float
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorMessage)
    # check if each row of the matrix is of the same length
    # ... and if the divisor is 0 and raises an exception
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
