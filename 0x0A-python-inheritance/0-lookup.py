#!/usr/bin/python3
# 0-lookup.py

"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
    obj: object returned by the function
    Return: a list of object if true.
    """

    return dir(obj)
