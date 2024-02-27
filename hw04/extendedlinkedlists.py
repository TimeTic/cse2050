from linkedlist import Node, LinkedList, Any    # get linkedlist.py from lab

# Create the classes for this assignment below.
# question 1


class ReversableLinkedList(LinkedList):
    """a reverse linkedlist to add more in linkedlist"""

    def reverse(self) -> None:
        """to reverse directions of linkedlist"""
        previous_node = None
        current_node = self._head
        while current_node is not None:
            next_node = current_node.link
            current_node.link = previous_node
            previous_node = current_node
            current_node = next_node
        self._head, self._tail = self._tail, self._head


rLL1 = ReversableLinkedList('abcd')
print(isinstance(rLL1, ReversableLinkedList))
print(isinstance(rLL1, LinkedList))
print(rLL1.get_head(), rLL1.get_tail())
rLL1.reverse()
print(rLL1.get_head(), rLL1.get_tail())
while rLL1:
    print(rLL1.remove_first())

# QUESTION 2


class SortedLinkedList(LinkedList):
    """sorted linkedlist to extend the linkedlist"""

    def add_first(self, item: Any) -> None:
        """to raise notimplementederror"""
        raise NotImplementedError(f"Use add_sorted({item}) instead")

    def add_last(self, item: Any) -> None:
        """to raise notimplementederror."""
        raise NotImplementedError(f"Use add_sorted({item}) instead")

    def add_sorted(self, item: Any) -> None:
        """insert item in the sorted linked list."""
        new_node = Node(item)
        if self._head is None or item <= self._head.item:
            new_node.link = self._head
            self._head = new_node
            if self._tail is None:
                self._tail = new_node
            self._size += 1
            return

        current_node = self._head
        while current_node.link is not None and current_node.link.item < item:
            current_node = current_node.link

        new_node.link = current_node.link
        current_node.link = new_node
        if new_node.link is None:
            self._tail = new_node
        self._size += 1


# Testing the SortedLinkedList class
sLL1 = SortedLinkedList()
print(isinstance(sLL1, SortedLinkedList))
print(isinstance(sLL1, LinkedList))
sLL1.add_sorted(8)
sLL1.add_sorted(8)
sLL1.add_sorted(3)
sLL1.add_sorted(11)
sLL1.add_sorted(1)
sLL1.add_sorted(9)
while sLL1:
    print(sLL1.remove_first())

# QUESTION 3


class UniqueLinkedList(LinkedList):
    """ unique linked list class that extends LinkedList"""

    def remove_dups(self) -> dict:
        """to remove duplicate items from the linked list and return dictionary of the removed items."""
        item_count = {}
        current_node = self._head
        previous_node = None

        while current_node is not None:
            if current_node.item in item_count:
                item_count[current_node.item] += 1

                if previous_node is not None:
                    previous_node.link = current_node.link
                else:
                    self._head = current_node.link

                if current_node is self._tail:
                    self._tail = previous_node
                current_node = current_node.link
            else:
                item_count[current_node.item] = 0
                previous_node = current_node
                current_node = current_node.link

        self._size -= sum(item_count.values())
        return item_count


# Testing the UniqueLinkedList class
uLL1 = UniqueLinkedList(['d', 'a', 'd', 'b'])
print(isinstance(uLL1, UniqueLinkedList))
print(isinstance(uLL1, LinkedList))
print(len(uLL1))
print(uLL1.get_head())
print(uLL1.get_tail())
print(uLL1.remove_dups())
while uLL1:
    print(uLL1.remove_first())