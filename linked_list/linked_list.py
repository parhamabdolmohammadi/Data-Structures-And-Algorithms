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
