#!/usr/bin/python3
# 6-load_from_json_file.py

"""
This module provides a function for saving an object to a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    filename: the name of the file to write to.
    """
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
