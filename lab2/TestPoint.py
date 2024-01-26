import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """ points for testing"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)
        self.p3 = Point(3,4)
    
    def test_init(self):
        """to test if two points are in the same attributes"""
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)

    def test_equidistant(self):
        """To test if two attributes has the same distance from the origin"""
        self.assertTrue(self.p1.equidistant(self.p3))
        self.assertTrue(Point(4, 3).equidistant(Point(3, 4)))
        self.assertFalse(self.p1.equidistant(self.p2))    


    def test_within(self):
        """this for testing if a point is within some distance of another point"""
        self.assertTrue(self.p1.within(5, self.p2))
        self.assertFalse(self.p1.within(1, self.p2))

if __name__ == '__main__':

    unittest.main()
# print("Hello WOl")
