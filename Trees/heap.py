from numbers import Number
import sys


class Heap:
    """
    Max Heap implemented using an array.

    Main interview complexities:
        Insert: O(log n)
        Remove max/root: O(log n)
        Peek max/root: O(1) if implemented
        Heapify: O(n)
        kth largest using heap inserts: O(n log n + k log n)
        Space: O(n)
    """

    def __init__(self):
        """
        Create an empty heap with initial capacity 10.

        Time: O(1)
        Space: O(1) initially, but heap can grow to O(n).
        """
        self.__array = [None] * 10
        self.__size = 0

    def insert(self, item: Number):
        """
        Insert a number into the max heap.

        Steps:
            1. Add item at the end.
            2. Bubble it up until heap property is restored.

        Time:
            O(log n)

        Space:
            O(1), ignoring resize.
            O(n) during resize.
        """

        if not isinstance(item, Number):
            raise TypeError("The item should be number")

        if self.__size == len(self.__array):
            new_array = [None] * (len(self.__array) * 2)

            for index, item in enumerate(self.__array):
                new_array[index] = item

            self.__array = new_array

        self.__array[self.__size] = item
        self.__size = self.__size + 1

        self.__bubble_up(self.__size - 1)

    def remove(self):
        """
        Remove and return the max/root value.

        Steps:
            1. Save root.
            2. Move last item to root.
            3. Remove last item.
            4. Bubble root down.

        Time:
            O(log n)

        Space:
            O(1)
        """
        if self.__size == 0:
            return None

        root = self.__array[0]

        self.__array[0] = self.__array[self.__size - 1]
        self.__array[self.__size - 1] = None
        self.__size -= 1

        if self.__size > 0:
            self.__bubble_down(0)

        return root

    @staticmethod
    def heapify(array: list) -> None:
        """
        Convert an array into a max heap in-place.

        Starts from the last parent and bubbles down each parent.

        Time:
            O(n)

        Space:
            O(1)
        """
        last_parent = (len(array) // 2) - 1

        for index in range(last_parent, -1, -1):
            Heap.__bubble_down_array(array, index)

    @staticmethod
    def __bubble_down_array(array: list, index: int) -> None:
        """
        Bubble down an item inside a normal array during heapify.

        Time:
            O(log n)

        Space:
            O(1)
        """
        size = len(array)

        while True:
            left_index = index * 2 + 1
            right_index = index * 2 + 2

            if left_index >= size:
                break

            if right_index >= size:
                larger_child_index = left_index
            else:
                larger_child_index = (
                    left_index
                    if array[left_index] > array[right_index]
                    else right_index
                )

            if array[index] >= array[larger_child_index]:
                break

            array[index], array[larger_child_index] = (
                array[larger_child_index],
                array[index]
            )

            index = larger_child_index

    @staticmethod
    def get_kth_largest_number(array, kth):
        """
        Return the kth largest number using a max heap.

        Example:
            kth = 1 returns largest.
            kth = 2 returns second largest.

        Time:
            Building heap using repeated inserts: O(n log n)
            Removing kth times: O(k log n)
            Total: O((n + k) log n)

        Space:
            O(n)
        """
        if kth <= 0 or kth > len(array):
            raise IndexError("Kth is out of bound of array")

        heap = Heap()

        for item in array:
            heap.insert(item)

        number = None

        for i in range(kth):
            number = heap.remove()

        return number

    def __bubble_up(self, index):
        """
        Move a node upward until parent is larger.

        Used after insertion.

        Time:
            O(log n)

        Space:
            O(log n), because this version is recursive.
        """

        if index > 0 and self.__array[self.__parent_index(index)] < self.__array[index]:
            self.__swap(index, self.__parent_index(index))
            self.__bubble_up(self.__parent_index(index))

    def __parent_index(self, index):
        """
        Return parent index of a node.

        Formula:
            parent = (index - 1) // 2

        Time: O(1)
        Space: O(1)
        """
        return (index - 1) // 2

    def __swap(self, index, parent_index):
        """
        Swap two array elements.

        Time: O(1)
        Space: O(1)
        """
        self.__array[parent_index], self.__array[index] = self.__array[index], self.__array[parent_index]

    def __bubble_down(self, index):
        """
        Move a node downward until it is larger than its children.

        Used after removing the root.

        Time:
            O(log n)

        Space:
            O(log n), because this version is recursive.
        """

        left_child = self.__get_left_child(index)
        right_child = self.__get_right_child(index)

        if left_child[0] is None and right_child[0] is None:
            return

        if (right_child[0] is not None):
            candidate_child, candidate_index = (
                left_child
                if left_child[0] > right_child[0]
                else right_child
            )
        else:
            candidate_child, candidate_index = left_child

        if candidate_child > self.__array[index]:
            self.__swap(index, candidate_index)
            self.__bubble_down(candidate_index)

    def __get_right_child(self, index):
        """
        Return right child value and index.

        Right child formula:
            right = index * 2 + 2

        Time: O(1)
        Space: O(1)
        """
        try:
            return self.__array[self.__get_right_child_index(index)], self.__get_right_child_index(index)

        except IndexError:
            return None, -1

    def __get_left_child(self, index):
        """
        Return left child value and index.

        Left child formula:
            left = index * 2 + 1

        Time: O(1)
        Space: O(1)
        """
        try:
            return self.__array[self.__get_left_child_index(index)], self.__get_left_child_index(index)

        except IndexError:
            return None, -1

    def __get_left_child_index(self, index):
        """
        Return left child index.

        Time: O(1)
        Space: O(1)
        """
        return index * 2 + 1

    def __get_right_child_index(self, index):
        """
        Return right child index.

        Time: O(1)
        Space: O(1)
        """
        return index * 2 + 2

    def __str__(self):
        """
        Return heap contents as a string.

        Time:
            O(n)

        Space:
            O(n), because slicing creates a new list.
        """
        return f"{self.__array[:self.__size]}"

    def __iter__(self):
        """
        Allow iteration over actual heap values.

        Time:
            O(n) to iterate all values.

        Space:
            O(n), because slicing creates a new list.
        """
        return iter(self.__array[:self.__size])

    def __bool__(self):
        """
        Allow usage like:
            while heap:

        Time: O(1)
        Space: O(1)
        """
        return self.__size > 0


if __name__ == "__main__":
    heap = Heap()
    heap.insert(15)
    heap.insert(10)
    heap.insert(3)
    heap.insert(8)
    heap.insert(12)
    heap.insert(9)
    heap.insert(4)
    heap.insert(1)
    heap.insert(24)
    print(heap)

    array = [2, 3, 7, 4, 8, 9, 10, 199, 1, 200]
    Heap.heapify(array)
    print(array)
    while heap:
        print(heap.remove())

    # for index, item in enumerate(heap):
    #     print(index, item)
