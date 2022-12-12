# for queue data type

from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

from queues import Queue
fifo =  Queue("1st", "2nd", "3rd")
len(fifo)

for element in fifo:
    print (element)

len(fifo)

#for building stack data type

class Stack(Queue):
    def dequeue (self):
        return self._elements.pop()

from queues import Stack

lifo = Stack("1st","2nd", "3rd")
for element in lifo:
    print (element)


lifo = []
lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")
lifo.pop()
lifo.pop()
lifo.pop()

#for representing priority queques with a heap

from heapq import heappush

fruits = []
heappush(fruits,"orange")
heappush(fruits,"apple")
heappush(fruits,"banana")
fruits

from heapq import heappop
heappop(fruits)
fruits

person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

person1 < person2
person2 < person3

#for building a priority queue data type

