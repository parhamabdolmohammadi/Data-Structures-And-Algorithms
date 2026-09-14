

def first_non_repeating_char(s: str):

    dict = {}

    for char in s:
        if char not in dict:
            dict[char] = 1

        else:
            dict[char] = dict[char] + 1

    for char in s:
        if dict[char] == 1:
            return char

    return -1


print(first_non_repeating_char("a green apple"))
