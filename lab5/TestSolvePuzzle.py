from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
    def testClockwise(self):
        """Tests a board solvable using only CW moves"""
        board = [3, 6, 4, 1, 3, 4, 2, 0]
        self.assertTrue(puzzle(board))
        
    def testCounterClockwise(self):
        """Tests a board solvable using only CCW moves"""
        board = [3, 4, 1, 2, 0]
        self.assertTrue(puzzle(board))
        
    def testMixed(self):
        """Tests a board solvable using only a combination of CW and CCW moves"""
        board = [2, 3, 1, 1, 4, 3, 1, 0]
        self.assertTrue(puzzle(board))
        
    def testUnsolvable(self):
        """Tests an unsolvable board"""
        board = [2, 3, 1, 1, 4, 3, 1, 1]
        self.assertFalse(puzzle(board))

if __name__ == '__main__':
    unittest.main()
