import unittest
from contains_permutation import contains_permutation

class permutation_pattern(unittest.TestCase):
    def test_contains_permutation(self):
        """this test cases checks where the input_string contains a permutation pattern """
        self.assertTrue(contains_permutation('abcdef', 'cab'))
        self.assertTrue(contains_permutation('keyboard', 'boy'))
       
    def test_does_not_contain_permutation(self):
        """"This test cases checks where input_string doesnt contain a permutation pattern"""
        self.assertFalse(contains_permutation('patriots', 'sit'))
        self.assertFalse(contains_permutation('apple', 'banana'))
