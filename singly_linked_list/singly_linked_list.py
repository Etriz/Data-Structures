class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def add_to_head(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
            return
        oldHead = self.head
        self.head = newNode
        self.head.next = oldHead
        self.length += 1

    def remove_tail(self):
        if self.head == None:
            return
        elif self.head == self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            return removed.value
        currentNode = self.head
        while currentNode:
            if currentNode.next == self.tail:
                value = self.tail.value
                currentNode.next = None
                self.tail = currentNode
                self.length -= 1
                return value
            currentNode = currentNode.next

    def remove_head(self):
        if self.head == None:
            return
        elif self.head == self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            return removed.value
        removed = self.head
        self.head = removed.next
        self.length -= 1
        return removed.value