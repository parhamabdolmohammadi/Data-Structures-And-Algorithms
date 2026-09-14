

from numbers import Number


class StringUtils:

    @staticmethod
    def count_vowels(value):
        if value is None:
            return -1

        value = str(value)

        vowels = ['a', 'o', 'u', 'e', 'i']
        count = 0

        for char in value:
            if char in vowels:
                count += 1

        return count

    @staticmethod
    def reverse_string(text):

        stack = []
        reversed_chars = []

        for char in text:
            stack.append(char)

        while stack:
            reversed_chars.append(stack.pop())

        return ''.join(reversed_chars)

    @staticmethod
    def reverse_words(str):
        word_list = str.split()

        reversed_words = list()

        while word_list:
            reversed_words.append(word_list.pop())

        return ' '.join(reversed_words)

    @staticmethod
    def are_rotations(str1, str2):

        if str1 is None or str2 is None:
            return False

        if len(str1) == len(str2) and str2 in (str1 + str1):
            return True

        return False

    @staticmethod
    def remove_duplicate(str):
        set = list()

        for char in str:
            if char not in set:
                set.append(char)

        return "".join(set)

    @staticmethod
    def most_repeated_char(text):

        dictionary = {}

        for char in text:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1

        highest = -1
        character = None

        for key, value in dictionary.items():
            if value > highest:
                highest = value
                character = key

        return character

    @staticmethod
    def capitalize(text):

        new_text = ""

        text_array = text.split(" ")

        for index, item in enumerate(text_array):

            if len(item) > 0:
                text_array[index] = item[0].upper() + item[1:]

        return " ".join(text_array)

    @staticmethod
    def are_anagrams(text1, text2):
        # print(sorted(text1))

        # print(text1)
        text_array1 = list(text1)
        text_array2 = list(text2)

        text_array1.sort()
        text_array2.sort()

        print(text_array1, text_array2)

        str1 = "".join(text_array1)
        str2 = "".join(text_array2)

        return str1 == str2

    @staticmethod
    def are_anagrams_hist(text1, text2):
        freq1 = {}
        freq2 = {}

        for char in text1:
            freq1[char] = freq1.get(char, 0) + 1

        for char in text2:
            freq2[char] = freq2.get(char, 0) + 1

        if len(freq1) != len(freq2):
            return False

        for key, value in freq1.items():

            if key not in freq2:
                return False

            if freq2[key] != value:
                return False

        return True

    @staticmethod
    def is_palindrome(text1):
        right = 0
        left = len(text1) - 1

        while right < left:
            if not text1[left] == text1[right]:
                return False

            right += 1
            left -= 1

        return True


print(StringUtils.count_vowels(1))
print(StringUtils.reverse_string("Jakesh"))
print(StringUtils.reverse_words("Aval  Dovom Zane "))
print(StringUtils.remove_duplicate("Parham"))
print(StringUtils.most_repeated_char("Paaarhhhhhhhhhhhhhhhhhhhhhaaaam"))
print(StringUtils.capitalize("ghasem Ghossame"))
print(StringUtils.are_anagrams("ABCCD", "CDCBA"))
print(StringUtils.is_palindrome("hseesh"))
