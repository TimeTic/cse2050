import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)
        self.p3 = Point(3,4)
    
    def test_init(self):
        """Tests that points are initialied with the correct attributes"""
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)

    def test_eq(self):
        """ADD YOUR OWN DOCSTRING"""
        self.assertEqual(self.p1,self.p3)
        self.assertNotEqual(self.p1, self.p2)


    def test_equidistant(self):
        """ADD YOUR OWN DOCSTRING"""
        self.assertEqual(self.p1,self.p3)
        self.assertEqual(self.p2.x, 5)

    def test_within(self):
        """ADD YOUR OWN DOCSTRING"""


unittest.main()
# print("Hello WOl")
