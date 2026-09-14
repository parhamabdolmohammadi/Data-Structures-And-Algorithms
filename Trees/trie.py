from numbers import Number


class IllegalStateException(Exception):
    pass


class Trie:

    class Node:
        def __init__(self, value, is_end):
            # Time: O(1)
            # Space: O(26) = O(1), because each node always stores 26 children
            self.__value = value
            self.__is_end = is_end
            self.__children = [None] * 26

        def __get_value(self):
            # Time: O(1)
            # Space: O(1)
            return self.__value

        def get_value(self):
            # Time: O(1)
            # Space: O(1)
            # Public getter needed for autocomplete.
            return self.__value

        def __set_value(self, value):
            # Time: O(1)
            # Space: O(1)
            if self.__value is not None:
                raise IllegalStateException("Value is Already is defined")
            elif not (isinstance(value, str) and len(value) == 1):
                raise IllegalStateException(
                    "Value should be a singular character")

            self.__value = value

        def set_is_end(self, value):
            # Time: O(1)
            # Space: O(1)
            if not isinstance(value, bool):
                raise IllegalStateException(
                    "Value Should be Boolean (True, False)")

            self.__is_end = value

        def is_end(self):
            # Time: O(1)
            # Space: O(1)
            return self.__is_end

        def get_children(self, index) -> "Trie.Node":
            # Time: O(1)
            # Space: O(1)
            self.index_type_check(index)
            self.index_bound_check(index)

            return self.__children[index]

        def get_children_list(self):
            # Time: O(1)
            # Space: O(1)
            return self.__children

        def get_children_value(self, index):
            # Time: O(1)
            # Space: O(1)
            self.index_type_check(index)
            self.index_bound_check(index)

            child = self.__children[index]
            return child.__get_value() if child else None

        def remove_child(self, index):
            # Time: O(1)
            # Space: O(1)
            self.index_type_check(index)
            self.index_bound_check(index)

            self.__children[index] = None

        def has_children(self):
            # Time: O(26) = O(1), because there are always 26 possible children
            # Space: O(1)
            for child in self.__children:
                if child is not None:
                    return True

            return False

        def set_children(self, index, value, is_end=False):
            # Time: O(1)
            # Space: O(1), creates one new Trie.Node
            self.index_type_check(index)
            self.index_bound_check(index)

            self.__children[index] = Trie.Node(value, is_end)

        def index_bound_check(self, index):
            # Time: O(1)
            # Space: O(1)
            if index >= 26:
                raise IllegalStateException("The index should be less than 26")

        def index_type_check(self, index):
            # Time: O(1)
            # Space: O(1)
            if not isinstance(index, Number):
                raise IllegalStateException("Index should be a number")

        def __str__(self):
            # Time: O(1)
            # Space: O(1)
            return f"Node({self.__value})"

    def __init__(self):
        # Time: O(1)
        # Space: O(1), root node has fixed 26 children
        self.__root = Trie.Node(None, False)

    def insert(self, word: str):
        # Time: O(n), where n is the length of the word
        # Space: O(n) in the worst case, if every character creates a new node

        current_node = self.__root
        last_index = len(word) - 1

        for index, char in enumerate(word):
            char_index = ord(char) - 97
            child = current_node.get_children_value(char_index)

            if child is None:
                current_node.set_children(char_index, char)

            current_node = current_node.get_children(char_index)

            if index == last_index:
                current_node.set_is_end(True)

    def contains(self, word):
        # Time: O(n), where n is the length of the word
        # Space: O(1), no extra structure is created

        current_node = self.__root
        is_end = None

        for char in word:
            char_index = ord(char) - 97
            child_val = current_node.get_children_value(char_index)
            child = current_node.get_children(char_index)

            if child_val != char:
                return False

            is_end = child.is_end()
            current_node = child

        return is_end

    def remove(self, word: str):
        # Time: O(n), where n is the length of the word
        # Space: O(n), because recursive calls go as deep as the word length
        self.__remove(self.__root, word, 0)

    def __remove(self, node, word, index):
        # Time: O(n), where n is the length of the word
        # Space: O(n), because this method is recursive

        if node is None:
            return False

        if index == len(word):
            if not node.is_end():
                return False

            node.set_is_end(False)
            return not node.has_children()

        char = word[index]
        char_index = ord(char) - 97

        child = node.get_children(char_index)

        should_delete_child = self.__remove(
            child,
            word,
            index + 1
        )

        if should_delete_child:
            node.remove_child(char_index)

            return (
                not node.is_end()
                and
                not node.has_children()
            )

        return False

    def autocomplete(self, prefix: str) -> list:
        # Time: O(p + k), where:
        # p = length of the prefix
        # k = total number of characters in all collected words
        # Space: O(k), because matching words are stored in a list

        current_node = self.__root

        for char in prefix:
            char_index = ord(char) - 97
            current_node = current_node.get_children(char_index)

            if current_node is None:
                return []

        words = []
        self.__collect_words(current_node, prefix, words)

        return words

    def __collect_words(self, node, prefix, words):
        # Time: O(k), where k is the total number of characters explored
        # Space: O(h), where h is the height of the remaining Trie branch
        # Extra space also includes the words list from autocomplete

        if node is None:
            return

        if node.is_end():
            words.append(prefix)

        children = node.get_children_list()

        for child in children:
            if child is not None:
                self.__collect_words(
                    child,
                    prefix + child.get_value(),
                    words
                )


if __name__ == "__main__":
    trie = Trie()

    # Insert test cases
    trie.insert("can")
    trie.insert("candy")
    trie.insert("cat")
    trie.insert("dog")

    # Contains test cases
    print(trie.contains("can"))        # Expected: True
    print(trie.contains("candy"))      # Expected: True
    print(trie.contains("cat"))        # Expected: True
    print(trie.contains("dog"))        # Expected: True
    print(trie.contains("ca"))         # Expected: False
    print(trie.contains("canada"))     # Expected: False

    # Autocomplete test cases
    print(trie.autocomplete("ca"))     # Expected: ['can', 'candy', 'cat']
    print(trie.autocomplete("can"))    # Expected: ['can', 'candy']
    print(trie.autocomplete("do"))     # Expected: ['dog']
    print(trie.autocomplete("z"))      # Expected: []

    # Remove test case 1: remove word that shares prefix with another word
    trie.remove("candy")
    print(trie.contains("candy"))      # Expected: False
    print(trie.contains("can"))        # Expected: True

    # Remove test case 2: remove shorter word while longer prefix branch was already removed
    trie.remove("can")
    print(trie.contains("can"))        # Expected: False
    print(trie.contains("cat"))        # Expected: True

    # Remove test case 3: remove a word that does not exist
    trie.remove("ghost")
    print(trie.contains("cat"))        # Expected: True
    print(trie.contains("dog"))        # Expected: True

    # Remove test case 4: remove independent word
    trie.remove("dog")
    print(trie.contains("dog"))        # Expected: False

    # Final autocomplete check after removals
    print(trie.autocomplete("ca"))     # Expected: ['cat']
