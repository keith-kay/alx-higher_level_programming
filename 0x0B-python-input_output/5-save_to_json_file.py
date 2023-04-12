#!/usr/bin/env python3
# 5-save_to_json_file.py

"""
This module provides a function for saving an object to a JSON file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    :my_obj: the object to write to the file.
    :filename: the name of the file to write to.
    """
    with open(filename,"w") as f:
        json.dump(my_obj, f)

