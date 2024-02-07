import unittest
from any_two_sum import any_two_sum

class TestAnyTwoSum(unittest.TestCase):
        """ this class is for a test case for the any_two_sum function in the  any_two_sum module"""
        def test_pos_result(self):
                """to test if test_pos_result function is postive"""
                result = any_two_sum([1, 3, 4, 5], 7)
                self.assertTrue(result)

        def test_neg_result(self):
                """to test if test_neg_restult has any negative numbers"""
                result = any_two_sum([1, 3, 4, 5], 2)
                self.assertFalse(result)
