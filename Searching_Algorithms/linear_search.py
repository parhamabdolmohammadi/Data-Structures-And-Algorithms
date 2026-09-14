import math
from numbers import Number


class Search:
    """
    A collection of common searching algorithms.

    Note:
        Most non-linear searches sort a copy of the original array first,
        so returned indexes refer to the sorted copy, not the original array.
    """

    def __init__(self, array):
        """
        Initialize the Search object.

        Args:
            array (list): The list of values to search through.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.__array = array

    def linear_search(self, number):
        """
        Search for a number by checking each element one by one.

        Args:
            number (Number): The value to search for.

        Returns:
            int: The index of the number if found, otherwise -1.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        for index, item in enumerate(self.__array):
            if item == number:
                return index
        return -1

    def binary_search(self, number):
        """
        Search for a number using recursive binary search.

        Note:
            Binary search requires a sorted array.

        Args:
            number (Number): The value to search for.

        Returns:
            int: The index of the number if found, otherwise -1.

        Time Complexity:
            O(log n)

        Space Complexity:
            O(log n) because of recursive call stack.
        """
        array = self.__array[:]
        array.sort()
        return self.__binary_search(number, array, 0, len(array) - 1)

    def __binary_search(self, number: Number, array, beg, end):
        """
        Helper method for recursive binary search.

        Args:
            number (Number): The value to search for.
            array (list): The sorted array.
            beg (int): Starting index.
            end (int): Ending index.

        Returns:
            int: The index of the number if found, otherwise -1.

        Time Complexity:
            O(log n)

        Space Complexity:
            O(log n) because of recursive call stack.
        """
        if beg > end:
            return -1

        mid_index = (beg + end) // 2

        if number < array[mid_index]:
            return self.__binary_search(number, array, beg, mid_index - 1)
        elif number > array[mid_index]:
            return self.__binary_search(number, array, mid_index + 1, end)
        else:
            return mid_index

    def binary_search_iterative(self, number):
        """
        Search for a number using iterative binary search.

        The array is copied and sorted before searching.

        Args:
            number (Number): The value to search for.

        Returns:
            int: The index of the number in the sorted array if found,
                 otherwise -1.

        Time Complexity:
            O(n log n) because of sorting.
            Search itself is O(log n).

        Space Complexity:
        O(1)
        """
        array = self.__array[:]
        array.sort()

        beg = 0
        end = len(array) - 1

        while beg <= end:
            mid_index = (beg + end) // 2

            if number < array[mid_index]:
                end = mid_index - 1
            elif number > array[mid_index]:
                beg = mid_index + 1
            else:
                return mid_index

        return -1

    def ternary_search(self, number):
        """
        Search for a number using recursive ternary search.

        The array is copied and sorted before searching.

        Args:
            number (Number): The value to search for.

        Returns:
            int: The index of the number in the sorted array if found,
                 otherwise -1.

        Time Complexity:
            O(n log n) because of sorting.
            Search itself is O(log3 n).

        Space Complexity:
            Space Complexity:
            O(log₃ n) because of recursive call stack.
        """
        array = self.__array[:]
        array.sort()
        return self.__ternary_search(number, array, 0, len(array) - 1)

    def __ternary_search(self, number, array, start, end):
        """
        Helper method for recursive ternary search.

        Args:
            number (Number): The value to search for.
            array (list): The sorted array.
            start (int): Starting index.
            end (int): Ending index.

        Returns:
            int: The index of the number if found, otherwise -1.

        Time Complexity:
            O(log3 n)

        Space Complexity:
            O(log3 n) because of recursive call stack.
        """
        if start > end:
            return -1

        partition_size = (end - start) // 3
        mid1 = start + partition_size
        mid2 = end - partition_size

        if number == array[mid1]:
            return mid1
        elif number == array[mid2]:
            return mid2
        elif number < array[mid1]:
            return self.__ternary_search(number, array, start, mid1 - 1)
        elif number > array[mid2]:
            return self.__ternary_search(number, array, mid2 + 1, end)
        else:
            return self.__ternary_search(number, array, mid1 + 1, mid2 - 1)

    def jump_search(self, number):
        """
        Search for a number using jump search.

        The array is copied and sorted before searching.
        The ideal block size is sqrt(n).

        Args:
            number (Number): The value to search for.

        Returns:
            int: The index of the number in the sorted array if found,
                 otherwise -1.

        Time Complexity:
        Best	O(1)
        Average	O(√n)
        Worst	O(√n)
        Space	O(1)
            O(n log n) because of sorting.
            Search itself is O(sqrt(n)).

        Space Complexity:
            O(1).
        """
        array = self.__array[:]
        array.sort()

        n = len(array)

        if n == 0:
            return -1

        block_size = int(math.sqrt(n))

        start = 0
        next_block = block_size

        while start < n and array[min(next_block, n) - 1] < number:
            start = next_block
            next_block += block_size

            if start >= n:
                return -1

        for i in range(start, min(next_block, n)):
            if array[i] == number:
                return i

        return -1

    def exponential_search(self, number):
        """
        Search for a number using exponential search.

        The array is copied and sorted before searching.
        Exponential search first finds a possible range, then applies
        binary search inside that range.

        Args:
            number (Number): The value to search for.

        Returns:
            int: The index of the number in the sorted array if found,
                 otherwise -1.

        Time Complexity:
            O(n log n) because of sorting. not considering sorting O(log n)
            Search itself is O(log n).

        Space Complexity:
            O(1) 
        """
        array = self.__array[:]
        array.sort()

        n = len(array)

        if n == 0:
            return -1

        if array[0] == number:
            return 0

        bound = 1

        while bound < n and array[bound] < number:
            bound *= 2

        left = bound // 2
        right = min(bound, n - 1)

        return self.__binary_search(number, array, left, right)


search = Search([3, 4, 6, 5, 3, 3, 2, 2])
print(search.binary_search(2))
print(search.ternary_search(4))
