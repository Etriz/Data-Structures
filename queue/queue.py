"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class ArrayQueue:  #! using array
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.append(value)

    def dequeue(self):
        if len(self.storage) == 0:
            return
        item = self.storage[0]
        self.storage.remove(item)
        return item


class Queue:  #! using linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        # current = self.head
        # length = 0
        # while current:
        #     length += 1
        #     current = current.next
        # return length
        return self.length

    def enqueue(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1

    def dequeue(self):
        if self.head == None:
            return
        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
