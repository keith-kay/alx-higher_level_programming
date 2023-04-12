#!/usr/bin/python3
# 9-student.py

class Student:
    def __init__(self, first_name, last_name, age):

        """Initializes a new Student instance with the given first name, last name, and age."""
      
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        
        """Returns a dictionary representation of the Student instance."""
        
        return self.__dict__.copy()

