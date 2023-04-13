#!/bin/usr/python3
# 2-is_same_class.py

"""Module containing is_same_class method"""

def is_same_class(obj, a_class):
    
    """Return True if obj is an instance of a_class, otherwise False"""

    return type(obj) == a_class
