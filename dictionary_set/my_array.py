

from numbers import Number


class Array:
    def __init__(self, size):
        self.index = 0
        self.size = size
        self.my_array = [None] * size

    def insert(self, number: Number):

        if (self.index) == len(self.my_array):
            self._grow()

        self.my_array[self.index] = number
        self.index += 1

    def remove_at(self, index: Number):
        if index < 0 or index >= self.index:
            return

        self.my_array[index] = None

        self._shrinkage(index)

    def index_of(self, number):

        for i in range(self.index):
            if self.my_array[i] == number:
                return i

        return None

    def _grow(self):
        self.size = self.size * 2
        new_array = [None] * self.size

        for i, value in enumerate(self.my_array):
            new_array[i] = value

        self.my_array = new_array

    def _shrinkage(self, index):

        for i, val in enumerate(self.my_array):
            if i <= index:
                continue

            self.my_array[i - 1] = val
            self.my_array[i] = None

        self.index -= 1

    def __str__(self):
        return str(self.my_array[0:self.index])


if __name__ == "__main__":
    my_array = Array(3)

    my_array.insert(3)
    my_array.insert(2)

    print(my_array)

    my_array.insert(1)

    print(my_array)

    my_array.insert(5)

    print(my_array)

    my_array.remove_at(3)

    print(my_array)
