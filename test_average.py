import unittest
from unittest import TestCase
from sarcina07 import *


class TestAverage(TestCase):
    def test_average(self):
        tests = [
            ([1, 2, 3, 4, 5], 3),
            ([1, 2, None, 4, 5], 2.4),
            ([None, 2, 3, 4, None], 1.8)
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(average(value), expected)


if __name__ == '__main__':
    unittest.main()
