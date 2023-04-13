#!/usr/bin/python3
# 1-my_list.py

"""
Class MyList Module
"""


class MyList(list):
    """Class MyList that inherits from list:"""

    def print_sorted(self):
        """
        Sort and print the list.
        """

        print(sorted(list(self)))
