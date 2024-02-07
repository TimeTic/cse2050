import unittest
from Linkedlist import Node

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node1 = Node('Jake', Node)
        self.node2  = Node('Amy')

    def test_node(self):
        self.assertEqual(self.node1.item, "Node('Jake')")
        self.assertEqual(self.node1.link,  None)

    # def test_repr(self):
    #     """to check the __repr__ method of a single item linked list"""
    #     self.assertEqual(self.node1.item, "Node(Jake)")
    #     self.assertEqual(self.node1.link,  Node)

unittest.main()