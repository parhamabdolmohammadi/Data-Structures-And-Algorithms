class Stack:

    def __init__(self):
        self.__stack = [None] * 5
        self.__size = 0

    def push(self, value):
        if self.__size % 5 == 0:
            self.__stack = self.__stack + ([None] * 5)

        self.__stack[self.__size] = value

        self.__size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Is empty")

        self.__size -= 1
        return self.__stack.pop(self.__size)

    def print(self):
        print(self.__stack[0:self.__size])

    def is_empty(self):
        return self.__size == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.__stack[self.__size - 1]

    def __str__(self):
        return str(self.__stack[0:self.__size])


class StackedQueue:

    def __init__(self):
        self.__stack1 = Stack()
        self.__stack2 = Stack()

    def enqueue(self, item):
        self.__stack1.push(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if self.__stack2.is_empty():
            while not self.__stack1.is_empty():
                self.__stack2.push(self.__stack1.pop())

        return self.__stack2.pop()

    def is_empty(self):
        return self.__stack1.is_empty() and self.__stack2.is_empty()


queue = StackedQueue()

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in range(0, 3):
    queue.enqueue(list[i])


print(queue.dequeue())


for i in range(3, 6):
    queue.enqueue(list[i])

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

for i in range(6, 8):
    queue.enqueue(list[i])

print(queue.dequeue())
print(queue.dequeue())

for i in range(8, 9):
    queue.enqueue(list[i])

print(queue.dequeue())
print(queue.dequeue())
