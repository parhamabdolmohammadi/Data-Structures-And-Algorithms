

def reverse_queue(queue: list):
    stack = list()

    while queue:
        stack.append(queue.pop(0))

    while stack:
        queue.append(stack.pop())

    return queue


azazel = reverse_queue(list("Hashem agha"))
print(azazel)
print("".join(azazel))
