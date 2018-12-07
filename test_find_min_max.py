from unittest import TestCase
from sarcina06 import *


class TestFind_min_max(TestCase):
    def test_find_min_max(self):
        # self.assertEqual(find_min_max(values), (-123, 566))
        self.assertEqual(find_min_max(values), (0, 0))
