

def balanced_expressions(str):
    opening_brackets = ["(", "<", "{", "["]
    closing_brackets = [")", ">", "}", "]"]

    str_brackets = []

    for char in str:

        if char in opening_brackets:
            str_brackets.append(char)

        if char in closing_brackets:
            if not str_brackets:
                return False

            opening_char = str_brackets.pop()
            opening_index = opening_brackets.index(opening_char)
            closing_index = closing_brackets.index(char)

            if not closing_index == opening_index:
                return False

    return len(str_brackets) == 0


print(balanced_expressions("{[<()"))
