import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc1), "Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")

    # Add more tests!


if __name__ == "__main__":
    unittest.main()
