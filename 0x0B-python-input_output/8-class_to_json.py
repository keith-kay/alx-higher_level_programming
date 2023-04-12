#!/usr/bin/python3
# 8-class_to_json.py


def class_to_json(obj):
    """ Function that returns the dictionary
    description with simple data structure
    obj: instance of class_to_json
    """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
