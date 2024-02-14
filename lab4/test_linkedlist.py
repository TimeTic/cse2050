# test_linkedlist.py

import unittest
from linkedlist import Node, LinkedList

class TestNode(unittest.TestCase):
    """this is for testing and initializing the object Node"""
    def setUp(self):
        """to initiliaze the node object"""
        self.node1 = Node('test', None)
        self.assertEqual(self.node1.item, 'test')
        self.assertIsNone(self.node1.link)

    def test_repr(self):
        """to test the string repr of the Node object"""
        node = Node('test', None)
        self.assertEqual(repr(node), "Node('test')")

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """this function tests thye empty linkedlist"""
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.get_head())
        self.assertIsNone(ll.get_tail())

    def test_add_first(self):
        """tests te addition of the node and  checks if it was added correctly."""
        ll = LinkedList()
        ll.add_first(1)
        ll.add_first(2)
        self.assertEqual(ll.get_head(), 2)
        self.assertEqual(ll.get_tail(), 1)
        self.assertEqual(len(ll), 2)

    def test_add_last(self):
        """this functinos tests the addition of node  at end of linkedlist"""
        ll = LinkedList()
        ll.add_last(1)
        ll.add_last(2)
        self.assertEqual(ll.get_head(), 1)
        self.assertEqual(ll.get_tail(), 2)
        self.assertEqual(len(ll), 2)

    def test_remove_first(self):
        """the test removes the first node fomr the linkedlist"""
        ll = LinkedList([1, 2, 3])
        self.assertEqual(ll.remove_first(), 1)
        self.assertEqual(ll.get_head(), 2)
        self.assertEqual(len(ll), 2)

    def test_remove_last(self):
        """tests removes the last node from the linkedlist"""
        ll = LinkedList([1, 2, 3])
        self.assertEqual(ll.remove_last(), 3)
        self.assertEqual(ll.get_tail(), 2)
        self.assertEqual(len(ll), 2)

if __name__ == '__main__':
    unittest.main()
