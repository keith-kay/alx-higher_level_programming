#!/usr/bin/python3
# 6-max_integer_test.py
""" Unittests for
test max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

# Creating a testcase by subclassing unittest.TestCase


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([1]), 1)

    def test_one_neg_element(self):
        """Test a list with a single negative element."""
        self.assertEqual(max_integer([-4]), -4)

    def test_neg(self):
        """Test a negative ordered list."""
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)

    def test_middle_element(self):
        """Test a middle place element in a list."""
        self.assertEqual(max_integer([1, 4, 6, 3, 5]), 6)


if __name__ == '__main__':
    unittest.main()
