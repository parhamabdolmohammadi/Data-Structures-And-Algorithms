
from linked_list import LinkedList
from numbers import Number


from linked_list import LinkedList
from numbers import Number


class HashTable:

    class Entry:
        def __init__(self, k, v):
            # Time: O(1)
            self.__key = k
            self.__value = v

        def get_key(self):
            # Time: O(1)
            return self.__key

        def get_value(self):
            # Time: O(1)
            return self.__value

        def __str__(self):
            # Time: O(1)
            return f"({self.__key}:{self.__value})"

        def set_value(self, val):
            # Time: O(1)
            self.__value = val

        def __eq__(self, entry):
            # Time: O(1)
            return (
                self.__key == entry.get_key()
                and self.__value == entry.get_value()
            )

    def __init__(self, size: Number):
        # Time: O(size)
        # Creates 'size' linked lists
        self.__dict = [LinkedList() for _ in range(size)]

    def put(self, k, v):
        # Average: O(1)
        # Worst case: O(n)

        # O(1)
        new_entry = HashTable.Entry(k, v)

        # O(1)
        index = self.__hash(k)

        # Average O(1), Worst O(n)
        if self.__already_in_list(k, v, index):
            pass
        else:
            # Usually O(1) if add_last is O(1)
            self.__dict[index].add_last(new_entry)

    def __already_in_list(self, k, v, index):
        # Average: O(1)
        # Worst case: O(n)

        linked_list = self.__dict[index]

        # Searches through one bucket
        for member in linked_list:
            entry = member.get_value()

            if entry.get_key() == k:
                self.__override(entry, v)
                return True

        return False

    def __override(self, entry: "HashTable.Entry", v):
        # Time: O(1)
        entry.set_value(v)

    def __hash(self, key):
        # Time: O(1)
        return key % len(self.__dict)

    def print(self):
        # Time: O(n)
        # Visits every bucket / stored item

        string = " \n"

        for item in self.__dict:
            string += str(item)
            string += ", \n"

        string = string[0:len(string) - 3] + string[len(string) - 2]

        print(f"\n[{string}\n]")

    def get(self, k):
        # Average: O(1)
        # Worst case: O(n)

        # O(1)
        index = self.__hash(k)

        linked_list = self.__dict[index]

        # Search through bucket
        for node in linked_list:

            entry = node.get_value()

            if entry.get_key() == k:
                return entry.get_value()

        raise KeyError(f"Key {k} doesnt exist in dict!")

    def remove(self, k):
        # Average: O(1)
        # Worst case: O(n)

        # O(1)
        index = self.__hash(k)

        linked_list = self.__dict[index]

        # Search through bucket
        for node in linked_list:

            entry = node.get_value()

            if entry.get_key() == k:
                # delete may also be O(n),
                # depending on your LinkedList implementation
                linked_list.delete(entry)
                return


dict = HashTable(5)

for i in range(1, 21):
    dict.put(i, i * 10)

# dict.print()


print(dict.get(2))
print(dict.get(8))
print(dict.get(14))
print(dict.get(20))
print(dict.get(1))

dict.remove(14)

dict.print()


dict.remove(20)
dict.print()
