#!/usr/bin/python3
# 11-student.py


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance with the given first name, last name, and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if not isinstance(attrs, list) or \
           not all(isinstance(i, str) for i in attrs):

            dic = self.__dict__.copy()
        else:

            dic = {i: self.__dict__[i] for i in attrs if i in self.__dict__}

        return dic

    def reload_from_json(self, json):
        
        for i in json:
            self.__dict__[i] = json[i]
