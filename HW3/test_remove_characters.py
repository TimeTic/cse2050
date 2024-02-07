import unittest
from remove_characters import remove_characters

class TestRemoveCharacters(unittest.TestCase):
    """this clas TestRemoveCharacters inherits from unittest.TestCase to create test methods for the remove_characters function to test my code """
    def test_remove_single_character(self):
        """this function is a test method to test the remove_characters function with a single character to remove  """
        result = remove_characters('abcd', 'c')
        self.assertEqual(result, 'abd')

    def test_remove_multiple_characters(self):
        """ this fucntion is another test method to test the remove_characters function with multiple characters to remove  """
        result = remove_characters('abcdefg', 'cf')
        self.assertEqual(result, 'abdeg')