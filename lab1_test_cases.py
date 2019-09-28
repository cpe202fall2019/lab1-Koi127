import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1, 2, 3]), 3)  # check all positive
        self.assertEqual(max_list_iter([-1, -2, -3]), -1)  # check neg
        self.assertEqual(max_list_iter([]), None)  # check empty array
        self.assertEqual(max_list_iter([1]), 1)  # check array with only one item
        self.assertEqual(max_list_iter([23, 23, 23]), 23)  # check array with equal numbers

    def test_reverse_rec(self):
        none_list = None
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])  # check all positive
        self.assertEqual(reverse_rec([-1, 2, 3, -10]), [-10, 3, 2, -1])  # check array with neg number
        self.assertEqual(reverse_rec([]), None)  # check empty array
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(none_list)

    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)  # check all positive
        list_val2 = []
        self.assertEqual(bin_search(4, 0, len(list_val2)-1, list_val2), None)  # check empty array
        list_val3 = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0, 0, 0, list_val3)
        list_val4 = [3, 3, 3, 3, 3, 3]
        self.assertEqual(bin_search(3, 0, len(list_val4)-1, list_val4), 3)  # check array with same number
        list_val5 = [-6, -4]
        self.assertEqual(bin_search(-6, 0, len(list_val5)-1, list_val5), 0)  # check array with 2 neg number
        list_val6 = [-6]
        self.assertEqual(bin_search(-6, 0, len(list_val6) - 1, list_val6), 0)  # check array with 1 neg number
        list_val7 = [-6, 0, 8, 9]
        self.assertEqual(bin_search(5, 0, len(list_val7) - 1, list_val7), None)  # check if not found


if __name__ == "__main__":
    unittest.main()
