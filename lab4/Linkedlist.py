# not finish a version
from typing import Any, Iterable, Optional

class Node:
    """ This class is representing a node in the list"""
    def __init__(self, item: Any, link: Optional['Node'] = None) -> None:
        """This function is intializing a new node object and this function is taking parameters such as Item Any, link:optional Node"""
        self.item = item
        self.link = link

    def __repr__(self) -> str:
        """This returns a string repr of the node object"""
        return f"Node({self.item})"
class LinkedList:
    """class representing linked list"""
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        """initiliazes a new linkedlist object and takes parameters such as: item: Optional[Iterabke[Any]]"""
        self._head = None
        self._tail = None
        self._size = 0

        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self) -> int:
        """This function is returing the number of items that are in linked list, 
        it returns -int: 
        """
        return self._size

    def get_head(self) -> Any:
        """returns head element from the linked list."""
        return self._head.item if self._head else None

    def get_tail(self) -> Any:
        """returns tail element from the linked list."""
        return self._tail.item if self._tail else None
    
    def add_first(self, item: Any) -> None:
        """this function adds an item to the beginning of the linked list."""
        new_node = Node(item)
        if not self._head:
            self._head = self._tail = new_node
        else:
            new_node.link = self._head
            self._head = new_node
        self._size += 1

    def add_last(self, item: Any) -> None:
        """this add-last function adds an item to the end of the linked list."""
        new_node = Node(item)
        if not self._head:
            self._head = self._tail = new_node
        else:
            self._tail.link = new_node
            self._tail = new_node
        self._size += 1
    
    def remove_first(self) -> Any:
        """the remove_first function removes and return the first item (head) of this list. If the list is empty"""
        if not self._head:
            raise RuntimeError()
        item = self._head.item
        if self._head is self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.link
        self._size -= 1
        return item

    def remove_last(self) -> Any:
        """the removee_last removes and retunrs items stored in tail node """
        if not self._head:
            raise RuntimeError()
        item = self._tail.item
        if self._head is self._tail:
            self._head = self._tail = None
        else:
            current = self._head
            while current.link is not self._tail:
                current = current.link
            current.link = None
            self._tail = current
        self._size -= 1
        return item