class Stack:

    def __init__(self):
        # Time: O(1)
        # Space: O(1) initially
        self.__stack = [None] * 5
        self.__size = 0

    def push(self, value):
        # Average: O(1)
        # Worst case: O(n) when resizing

        # O(1)
        self.__stack[self.__size] = value

        # O(1)
        self.__size += 1

        if self.__size % 5 == 0:
            # O(n) because a new list is created and
            # existing elements are copied
            self.__stack = self.__stack + ([None] * 5)

    def pop(self):
        # O(n) in your current implementation!

        if self.is_empty():
            raise IndexError("Stack is empty")

        # O(1)
        self.__size -= 1

        # O(n) because list.pop(index) may shift
        # all elements after this index
        return self.__stack.pop(self.__size)

    def print(self):
        # O(n)
        # Slicing creates a new list
        print(self.__stack[0:self.__size])

    def is_empty(self):
        # O(1)
        return self.__size == 0

    def peek(self):
        # O(1)

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.__stack[self.__size - 1]

    def __str__(self):
        # O(n)
        # Slicing + converting the elements to a string
        return str(self.__stack[0:self.__size])


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.print()
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.peek())
# print(stack.pop())
stack.print()
