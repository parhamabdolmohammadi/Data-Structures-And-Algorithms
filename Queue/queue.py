

from numbers import Number


class Queue:

    def __init__(self):
        self.__queue = [None] * 5
        self.__front = 0
        self.__rear = 0

    def enqueue(self, item: Number):

        if self.is_full():
            self.__queue = self.__queue + [None] * 5

        self.__queue[self.__rear] = item
        self.__rear += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")

        item = self.__queue[self.__front]
        self.__queue[self.__front] = None
        self.__front += 1
        return item

    def peek(self):
        return self.__queue[self.__front]

    def is_empty(self):
        return self.__rear == self.__front

    def is_full(self):
        return self.__rear == len(self.__queue)

    def __str__(self):

        return str(self.__queue[self.__front:self.__rear])


queue = Queue()

queue.enqueue(1)
print(queue)

queue.enqueue(1)
print(queue)

queue.enqueue(1)
print(queue)

queue.enqueue(1)
print(queue)

queue.enqueue(1)
print(queue)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue)

queue.enqueue(1)
queue.enqueue(1)
print(queue)

queue.enqueue(1)
print(queue)
queue.enqueue(1)
print(queue)
