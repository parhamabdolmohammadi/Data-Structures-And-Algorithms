class EmptyLinkedListException(Exception):
    pass


class LinkedList:

    class Node:
        def __init__(self, value):
            # Time: O(1)
            # Space: O(1)
            self.__value = value
            self.__next = None

        def get_value(self):
            # Time: O(1)
            # Space: O(1)
            return self.__value

        def set_value(self, value):
            # Time: O(1)
            # Space: O(1)
            self.__value = value

        def get_next(self):
            # Time: O(1)
            # Space: O(1)
            return self.__next

        def set_next(self, node):
            # Time: O(1)
            # Space: O(1)
            self.__next = node

        def __str__(self):
            # Time: O(1)
            # Space: O(1)
            return str(self.__value)

    def __init__(self):
        # Time: O(1)
        # Space: O(1)
        self.__first = None
        self.__last = None
        self.__size = 0

    def is_empty(self):
        # Time: O(1)
        # Space: O(1)
        return self.__first is None

    def size(self):
        # Time: O(1)
        # Space: O(1)
        return self.__size

    def add_first(self, value):
        # Time: O(1)
        # Space: O(1)

        new_node = LinkedList.Node(value)

        if self.is_empty():
            self.__first = new_node
            self.__last = new_node
        else:
            new_node.set_next(self.__first)
            self.__first = new_node

        self.__size += 1

    def add_last(self, value):
        # Time: O(1)
        # Space: O(1)

        new_node = LinkedList.Node(value)

        if self.is_empty():
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.set_next(new_node)
            self.__last = new_node

        self.__size += 1

    def remove_first(self):
        # Time: O(1)
        # Space: O(1)

        if self.is_empty():
            raise EmptyLinkedListException("Linked List is Empty")

        removed_value = self.__first.get_value()

        if self.__first == self.__last:
            self.__first = None
            self.__last = None
        else:
            self.__first = self.__first.get_next()

        self.__size -= 1

        return removed_value

    def remove_last(self):
        # Time: O(n)
        # Space: O(1)

        if self.is_empty():
            raise EmptyLinkedListException("Linked List is Empty")

        removed_value = self.__last.get_value()

        if self.__first == self.__last:
            self.__first = None
            self.__last = None
        else:
            previous = self.__first

            while previous.get_next() != self.__last:
                previous = previous.get_next()

            previous.set_next(None)
            self.__last = previous

        self.__size -= 1

        return removed_value

    def contains(self, value):
        # Time: O(n)
        # Space: O(1)

        current = self.__first

        while current is not None:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def index_of(self, value):
        # Time: O(n)
        # Space: O(1)

        current = self.__first
        index = 0

        while current is not None:
            if current.get_value() == value:
                return index

            current = current.get_next()
            index += 1

        return -1

    def remove_value(self, value):
        # Time: O(n)
        # Space: O(1)

        if self.is_empty():
            return False

        # Removing first node
        if self.__first.get_value() == value:
            self.remove_first()
            return True

        previous = self.__first
        current = self.__first.get_next()

        while current is not None:
            if current.get_value() == value:

                # Removing last node
                if current == self.__last:
                    self.__last = previous

                previous.set_next(current.get_next())
                self.__size -= 1
                return True

            previous = current
            current = current.get_next()

        return False

    def reverse(self):
        # Time: O(n)
        # Space: O(1)

        if self.is_empty():
            return

        previous = None
        current = self.__first
        self.__last = self.__first

        while current is not None:
            next_node = current.get_next()

            current.set_next(previous)

            previous = current
            current = next_node

        self.__first = previous

    def to_list(self):
        # Time: O(n)
        # Space: O(n)

        result = []

        current = self.__first

        while current is not None:
            result.append(current.get_value())
            current = current.get_next()

        return result

    def clear(self):
        # Time: O(1)
        # Space: O(1)

        self.__first = None
        self.__last = None
        self.__size = 0

    def __iter__(self):
        # Time: O(1)
        # Space: O(1)

        current = self.__first

        while current is not None:
            yield current.get_value()
            current = current.get_next()

    def __str__(self):
        # Time: O(n)
        # Space: O(n)

        values = []

        current = self.__first

        while current is not None:
            values.append(str(current.get_value()))
            current = current.get_next()

        return " -> ".join(values)


if __name__ == "__main__":

    linked_list = LinkedList()

    # ---------------- ADD TESTS ----------------

    linked_list.add_last(10)
    linked_list.add_last(20)
    linked_list.add_last(30)

    print(linked_list)  # Expected: 10 -> 20 -> 30

    linked_list.add_first(5)

    print(linked_list)  # Expected: 5 -> 10 -> 20 -> 30

    # ---------------- SIZE TEST ----------------

    print(linked_list.size())  # Expected: 4

    # ---------------- CONTAINS TESTS ----------------

    print(linked_list.contains(20))  # Expected: True
    print(linked_list.contains(99))  # Expected: False

    # ---------------- INDEX TESTS ----------------

    print(linked_list.index_of(30))  # Expected: 3
    print(linked_list.index_of(100))  # Expected: -1

    # ---------------- REMOVE FIRST TEST ----------------

    removed = linked_list.remove_first()

    print(removed)      # Expected: 5
    print(linked_list)  # Expected: 10 -> 20 -> 30

    # ---------------- REMOVE LAST TEST ----------------

    removed = linked_list.remove_last()

    print(removed)      # Expected: 30
    print(linked_list)  # Expected: 10 -> 20

    # ---------------- REMOVE VALUE TESTS ----------------

    linked_list.add_last(40)
    linked_list.add_last(50)

    print(linked_list)  # Expected: 10 -> 20 -> 40 -> 50

    linked_list.remove_value(20)

    print(linked_list)  # Expected: 10 -> 40 -> 50

    linked_list.remove_value(50)

    print(linked_list)  # Expected: 10 -> 40

    print(linked_list.remove_value(999))  # Expected: False

    # ---------------- REVERSE TEST ----------------

    linked_list.reverse()

    print(linked_list)  # Expected: 40 -> 10

    # ---------------- TO LIST TEST ----------------

    print(linked_list.to_list())  # Expected: [40, 10]

    # ---------------- ITERATOR TEST ----------------

    for item in linked_list:
        print(item)

    # Expected:
    # 40
    # 10

    # ---------------- CLEAR TEST ----------------

    linked_list.clear()

    print(linked_list.is_empty())  # Expected: True
    print(linked_list.size())      # Expected: 0
