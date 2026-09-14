from numbers import Number
from my_array import Array


class LinkedList:
    """
    A simple implementation of a singly linked list.

    Attributes:
        first (Node): Reference to the first node in the list.
        last (Node): Reference to the last node in the list.
    """

    class Node:
        """
        A representation of the Linked list node ass inner class
        """

        def __init__(self, value):
            """
            initialization of empty 
            """
            self.__value = value
            self.__next: LinkedList.Node = None

        def get_value(self) -> Number:
            """
            value getter
            """
            return self.__value

        def set_next(self, node: "LinkedList.Node"):
            """
            Setter for the next node
            """
            self.__next = node

        def get_next(self):
            """
            Getter for next Node
            """
            return self.__next

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.__first: LinkedList.Node = None
        self.__last: LinkedList.Node = None
        self.__size = 0

    def add_first(self, value):
        """
        Insert a new node at the beginning of the linked list.

        Updates the 'first' pointer and, if the list was empty,
        also updates the 'last' pointer.
        """

        if self.__first is None:
            self.add_last(value)
        else:
            new_node = LinkedList.Node(value)

            new_node.set_next(self.__first)
            self.__first = new_node
            self.__size += 1

    def add_last(self, value: Number) -> None:
        """
        Insert a new node at the end of the linked list.

        Updates the 'last' pointer and, if the list was empty,
        also updates the 'first' pointer.
        """
        new_node = LinkedList.Node(value)

        if self.__first is None:
            self.__first = self.__last = new_node
        else:
            self.__last.set_next(new_node)
            self.__last = new_node

        self.__size += 1

    def delete_first(self):
        """
        Remove the first node from the linked list.

        Updates the 'first' pointer. If the list becomes empty,
        also updates the 'last' pointer.
        """

        if self.__first is None:
            return

        current_node = self.__first

        if current_node.get_next() is not None:
            self.__first = self.__first.get_next()
        else:
            self.__first = None
            self.__last = None

        self.__size -= 1

    def delete_last(self):
        """
        Remove the last node from the linked list.

        Updates the 'last' pointer. If the list becomes empty,
        also updates the 'first' pointer.
        """
        if self.__first is None:
            return

        if self.__first == self.__last:
            self.__first = None
            self.__last = None
        else:
            current_node = self.__first
            last_node = None

            while current_node != self.__last:
                last_node = current_node
                current_node = current_node.get_next()

            last_node.set_next(None)
            self.__last = last_node

        self.__size -= 1

    def contains(self, value):
        """
        Check whether a given value exists in the linked list.

        Returns:
            bool: True if the value is found, False otherwise.
        """

        next_node: LinkedList.Node = self.__first

        while next_node is not None:
            val = next_node.get_value()

            if value == val:
                return True

            next_node = next_node.get_next()

        return False

    def to_array(self):
        """
        Turn the array into a linkedlist
        """
        new_array = Array(self.__size)

        current = self.__first

        while current is not None:
            new_array.insert(current.get_value())
            current = current.get_next()

        return new_array

    def index_of(self, value: Number):
        """
        Find the index of a given value in the linked list.

        Returns:
            int: The index of the value if found, otherwise -1.
        """
        index = 0
        next_node: LinkedList.Node = self.__first

        while next_node is not None:
            val = next_node.get_value()

            if value == val:
                return index

            next_node = next_node.get_next()
            index += 1

        index = -1
        return index

    def reverse(self):
        """
        Reverse the linked list
        """

        if self.__first is None:
            return

        previous = None
        current = self.__first

        while current is not None:
            next = current.get_next()
            current.set_next(previous)

            previous = current
            current = next

        self.__last = self.__first
        self.__first = previous

    def kth_node_end(self, number: Number):
        if number > self.__size:
            raise Exception(
                f"The number should be less than size: {self.__size}")

        if number <= 0:
            raise Exception(f"The number should be more than zero")

        first = self.__first

        for i in range(1, number):
            first = first.get_next()

        second = self.__first

        while first.get_next() is not None:
            first = first.get_next()
            second = second.get_next()

        return second.get_value()

    def print(self):
        """
        print the string representation of the linkedlist
        """
        string = ""
        next_node: LinkedList.Node = self.__first

        while next_node is not None:
            string += str(next_node.get_value())
            next_node = next_node.get_next()

            if next_node is not None:
                string += " -> "

        print(f"{{{string}}} The size ({self.__size})")


linked_list = LinkedList()

linked_list.add_last(10)
linked_list.add_last(20)
linked_list.add_first(40)
linked_list.add_last(30)
linked_list.add_first(50)
linked_list.print()

print(linked_list.index_of(50))
print(linked_list.index_of(10))
print(linked_list.index_of(555))

print(linked_list.contains(50))
print(linked_list.contains(10))
print(linked_list.contains(555))

linked_list.delete_first()
linked_list.delete_first()
linked_list.delete_first()
linked_list.print()

linked_list.add_last(10)
linked_list.add_last(20)
linked_list.add_first(40)
linked_list.print()

print("hello")

linked_list.delete_last()
linked_list.delete_last()
linked_list.delete_last()
linked_list.print()

print(linked_list.to_array())

linked_list.add_last(10)
linked_list.add_last(20)
linked_list.add_first(40)
linked_list.print()

linked_list.reverse()
linked_list.print()

print(linked_list.kth_node_end(5))
