

class SortingAlgorithms:
    """
    A collection of common sorting algorithms.
    """

    def __init__(self, array):
        """
        Initialize the SortingAlgorithms object.

        Args:
            array (list): The list to sort.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.__array = array

    def bubble_sort(self):
        """
        Sort the array using Bubble Sort.

        Bubble Sort repeatedly compares adjacent elements
        and swaps them if they are in the wrong order.

        Returns:
            list: The sorted array.

        Time Complexity:
            Best: O(n)
            Average: O(n²)
            Worst: O(n²)

        Space Complexity:
            O(1)
        """
        i = 0

        array_length = len(self.__array)
        array = self.__array[:]

        while i < array_length:

            for index in range(array_length - 1):

                if array[index] > array[index + 1]:
                    current = array[index]
                    array[index] = array[index + 1]
                    array[index + 1] = current

            i += 1

        return array

    def selection_sort(self):
        """
        Sort the array using Selection Sort.

        Selection Sort repeatedly finds the minimum element
        and places it in its correct position.

        Returns:
            list: The sorted array.

        Time Complexity:
            Best: O(n²)
            Average: O(n²)
            Worst: O(n²)

        Space Complexity:
            O(1)
        """
        array = self.__array[:]
        n = len(array)

        for index in range(n):
            min_index = index

            for i in range(index + 1, n):
                if array[i] < array[min_index]:
                    min_index = i

            if min_index != index:
                array[index], array[min_index] = array[min_index], array[index]

        return array

    def insertion_sort(self):
        """
        Sort the array using Insertion Sort.

        Insertion Sort builds a sorted portion of the array
        by inserting each element into its proper position.

        Returns:
            list: The sorted array.

        Time Complexity:
            Best: O(n)
            Average: O(n²)
            Worst: O(n²)

        Space Complexity:
            O(1)
        """

        n = len(self.__array)

        for i in range(1, n):
            current = self.__array[i]
            j = i - 1

            while j >= 0 and self.__array[j] > current:
                self.__array[j + 1] = self.__array[j]
                j -= 1

            self.__array[j + 1] = current

        return self.__array

    def merge_sort(self):
        """
        Sort the array using Merge Sort.

        Merge Sort recursively divides the array into halves,
        sorts them, and merges them together.

        Returns:
            list: The sorted array.

        Time Complexity:
            Best: O(n log n)
            Average: O(n log n)
            Worst: O(n log n)

        Space Complexity:
            O(n)
        """

        new_array = self.__array[:]
        return self.__merge_sort(new_array)

    def __merge_sort(self, array):
        """
        Recursive helper method for Merge Sort.

        Args:
            array (list): The array or subarray to sort.

        Returns:
            list: Sorted subarray.

        Time Complexity:
            O(n log n)

        Space Complexity:
            O(n)
        """

        if len(array) < 2:
            return array

        middle_index = len(array) // 2

        first_sub = array[:middle_index]
        second_sub = array[middle_index:]

        first_sub = self.__merge_sort(first_sub)
        second_sub = self.__merge_sort(second_sub)

        index_first = 0
        index_second = 0

        new_array = []

        while (index_first < len(first_sub)
               and
               index_second < len(second_sub)):

            if first_sub[index_first] < second_sub[index_second]:
                new_array.append(first_sub[index_first])
                index_first += 1

            else:
                new_array.append(second_sub[index_second])
                index_second += 1

        while index_first < len(first_sub):
            new_array.append(first_sub[index_first])
            index_first += 1

        while index_second < len(second_sub):
            new_array.append(second_sub[index_second])
            index_second += 1

        return new_array

    def quick_sort(self):
        """
        Sort the array using Quick Sort.

        Quick Sort selects a pivot element and partitions
        the array around the pivot recursively.

        Returns:
            list: The sorted array.

        Time Complexity:
            Best: O(n log n)
            Average: O(n log n)
            Worst: O(n²) age partition hamash ye item invar hame onvaresh

        Space Complexity:
            Best/Average: O(log n)
            Worst: O(n)
            But the space complexity isn't O(1) because of recursion. Every recursive function call uses memory on the call stack.
        """
        array = self.__array[:]
        self.__quick_sort(array, 0, len(array) - 1)
        return array

    def __quick_sort(self, array, start, end):
        """
        Recursive helper method for Quick Sort.

        Args:
            array (list): The array being sorted.
            start (int): Starting index.
            end (int): Ending index.

        Time Complexity:
            Best/Average: O(n log n)
            Worst: O(n²)

        Space Complexity:
            Best/Average: O(log n)
            Worst: O(n)
        """
        if start >= end:
            return

        pivot_index = self.__partition(array, start, end)

        self.__quick_sort(array, start, pivot_index - 1)
        self.__quick_sort(array, pivot_index + 1, end)

    def __partition(self, array, start, end):
        """
        Partition the array around a pivot element.

        Elements smaller than the pivot are moved to the left,
        and larger elements are moved to the right.

        Args:
            array (list): The array being partitioned.
            start (int): Starting index.
            end (int): Ending index.

        Returns:
            int: Final pivot index.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        pivot = array[end]

        i = start - 1

        for j in range(start, end):

            if array[j] < pivot:
                i += 1

                array[i], array[j] = array[j], array[i]

        array[i + 1], array[end] = array[end], array[i + 1]

        return i + 1

    def counting_sort(self, max):
        """
        Sort the array using Counting Sort.

        Counting Sort counts occurrences of each value
        and reconstructs the sorted array.

        Args:
            max (int): Maximum possible value in the array.

        Returns:
            list: The sorted array.

        Time Complexity:
            O(n + k)

        Space Complexity:
            O(k)

        Note:
            k = maximum value range.
        """
        array = self.__array
        counts = [0] * (max + 1)
        new_array = []

        for item in array:
            counts[item] = counts[item] + 1

        for index, item in enumerate(counts):
            counter = 0

            while counter < item:
                new_array.append(index)

                counter += 1

        return new_array

    def bucket_sort(self):
        """
        Sort the array using Bucket Sort.

        Time Complexity:
            Best/Average: O(n + k)
            Worst: O(n²)

        Space Complexity:
            O(n + k)

        k = number of buckets
        """

        array = self.__array[:]

        if len(array) == 0:
            return array

        n = len(array)

        # Textbook choice: use n buckets
        buckets = [[] for _ in range(n)]

        max_value = max(array)

        # Put each value into a bucket
        for item in array:

            bucket_index = int(
                item * (n - 1) / max_value
            )

            buckets[bucket_index].append(item)

        # Sort each bucket
        for i in range(n):
            buckets[i] = self.__merge_sort(buckets[i])

        # Merge all buckets
        sorted_array = []

        for bucket in buckets:
            sorted_array.extend(bucket)

        return sorted_array


sort = SortingAlgorithms([9, 5, 7, 2, 1, 98])

# print(sort.bubble_sort())
# print(sort.selection_sort())
# print(sort.insertion_sort())
# print(sort.merge_sort())
# print(sort.quick_sort())
# print(sort.counting_sort(98))
print(sort.bucket_sort())
