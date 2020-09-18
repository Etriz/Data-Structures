"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:  #! using array
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return
        return self.storage.pop()


class Stack02:  #! using linked list
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

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1

    def pop(self):
        if self.head == None:
            return
        if self.head.next == None:
            data = self.head.data
            self.head = None
            self.length -= 1
            return data
        previousNode = self.head
        while previousNode:
            if previousNode.next == self.tail:
                data = self.tail.data
                previousNode.next = None
                self.tail = previousNode
                self.length -= 1
                return data
            previousNode = previousNode.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None