import unittest
from lec1 import binary_search

class TestBinarySearcch(unittest.TestCase):
    def test_empty_list(self):
        L = []
        self.assertFalse(binary_search(L, 42), False)

    def test_false(self):
        L = [1, 2, 3, 4]
        for  item in range(5, 10):
            self.assertFalse(binary_search(L, item))

    def test_true(self):
        L = [1, 2, 3, 4]
        for item in L:
            self.assertTrue(binary_search(L, item))

    def test_large_list(self):
        L = list(range(200))
        for item in L:
            self.assertTrue(binary_search(L, item))
        