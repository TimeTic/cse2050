import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort


class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""

    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    #####################################################################################
    ################## implement the common test scenarios  #############################
    ############## empty list, sorted list, reverse sorted list, random list ############
    #####################################################################################
    def test_empty_list(self):
        """tets soring empty list"""
        arr = []
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertEqual(sorted_arr, [])
        self.assertEqual(num_swaps, 0)

    def test_sorted_list(self):
        """tests for sorting a sorted list"""
        arr = [1, 2, 3, 4, 5]
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertEqual(sorted_arr, arr)
        self.assertEqual(num_swaps, 0)

    def test_reverse_sorted_list(self):
        """tests for reversing a sorted list"""
        arr = [5, 4, 3, 2, 1]
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

        if self.sorting_alg in (bubble_sort, insertion_sort):
            self.assertEqual(num_swaps, 10)

    def test_random_list(self):
        """tests for sorting random list"""
        arr = [3, 4, 2, 1, 5]
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])


class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)


class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Test class for the insertion sort algorithm."""
    def setUp(self):
        """Set up the insertion sort algorithm for testing."""
        super().setUp(insertion_sort)


class TestSelection(SortingTestFactory, unittest.TestCase):
    """Test class for the selection sort algorithm."""
    def setUp(self):
        """Set up the selection sort algorithm for testing."""
        super().setUp(selection_sort)


if __name__ == "__main__":
    unittest.main()
