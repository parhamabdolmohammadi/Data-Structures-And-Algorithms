

def string_reverse(str):
    stack = []
    reversed_list = []

    for char in str:
        stack.append(char)

    while stack:
        char = stack.pop()
        print(char)
        reversed_list = reversed_list + list(char)

    print(reversed_list)


string_reverse("helooooooo")
