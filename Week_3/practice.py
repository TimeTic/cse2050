# # test_linkedlist.py

# import unittest
# from linkedlist import Node

# class TestNode(unittest.TestCase):
#     def test_init(self):
#         node = Node('test', None)
#         self.assertEqual(node.item, 'test')
#         self.assertIsNone(node.link)

#     def test_repr(self):
#         node = Node('test', None)
#         self.assertEqual(repr(node), "Node('test')")

# if __name__ == '__main__':
#     unittest.main()


# # linkedlist.py

# from typing import Any, Optional

# class Node:
#     def __init__(self, item: Any, link: Optional['Node'] = None) -> None:
#         self.item = item
#         self.link = link

#     def __repr__(self) -> str:
#         return f"Node({repr(self.item)})"

# # test_linkedlist.py

# import unittest
# from linkedlist import Node, LinkedList

# class TestLinkedList(unittest.TestCase):
#     def test_empty_init(self):
#         ll = LinkedList()
#         self.assertEqual(len(ll), 0)
#         self.assertIsNone(ll.get_head())
#         self.assertIsNone(ll.get_tail())

#     # Add more test cases here for other methods...

# if __name__ == '__main__':
#     unittest.main()


# # linkedlist.py

# from typing import Any, Iterable, Optional

# class Node:
#     def __init__(self, item: Any, link: Optional['Node'] = None) -> None:
#         self.item = item
#         self.link = link

#     def __repr__(self) -> str:
#         return f"Node({repr(self.item)})"

# class LinkedList:
#     def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
#         self._head = None
#         self._tail = None
#         self._size = 0

#         if items is not None:
#             for item in items:
#                 self.add_last(item)

#     def __len__(self) -> int:
#         return self._size

#     def get_head(self) -> Any:
#         return self._head.item if self._head else None

#     def get_tail(self) -> Any:
#         return self._tail.item if self._tail else None

#     # Implement other methods as per the specifications...

#     # Example implementation of add_last method
#     def add_last(self, item: Any) -> None:
#         new_node = Node(item)
#         if self._head is None:
#             self._head = new_node
#         else:
#             self._tail.link = new_node
#         self._tail = new_node
#         self._size += 1
