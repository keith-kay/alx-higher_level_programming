#!/usr/bin/python3
# 3-to_json_string.py

"""Importing JSON library"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string):"""
    return json.dumps(my_obj)
