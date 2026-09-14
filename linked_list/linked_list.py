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
