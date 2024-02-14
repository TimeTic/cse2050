import unittest
from find_factors import find_factors

class TestFindFactors(unittest.TestCase):
    def test_pdf(self):
        expected = {6: [6, 1, 3], 7: [7, 1], 18: [6, 18, 1, 3], 1: [1], 3: [1, 3]}
        L = [6, 7, 18, 1, 3]
        actual = find_factors(L)

        self.assertEqual(actual, expected)

    def test_empty(self):
        self.assertEqual(find_factors([]), dict())

    def test_duplicates(self):
        L = [1, 1, 1, 1, 1]
        expected = {1:[1, 1, 1, 1, 1]}
        self.assertEqual(find_factors(L), expected)

unittest.main()