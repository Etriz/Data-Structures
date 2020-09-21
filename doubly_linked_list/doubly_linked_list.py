"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length
        # return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        newNode = ListNode(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
            return
        oldHead = self.head
        self.head = newNode
        self.head.next = oldHead
        oldHead.prev = newNode
        self.length += 1
        return

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head == None:
            return
        elif self.head == self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed.value
        newHead = self.head.next
        removed = self.head
        self.head = newHead
        self.head.prev = None
        self.length -= 1
        return removed.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        newNode = ListNode(value)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
            return
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail == None:
            return
        elif self.tail == self.head:
            removed = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return removed.value
        removed = self.tail
        newTail = self.tail.prev
        self.tail = newTail
        self.tail.next = None
        self.length -= 1
        return removed.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        prevNode = node.prev
        nextNode = node.next
        oldHead = self.head
        oldHead.prev = node
        self.head = node
        self.head.next = oldHead
        self.head.prev = None
        if prevNode is not None:
            prevNode.next = nextNode
        if nextNode is not None:
            nextNode.prev = prevNode
        if self.tail == node:
            self.tail = prevNode
            self.tail = None

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.tail == node:
            return
        prevNode = node.prev
        nextNode = node.next
        oldTail = self.tail
        oldTail.next = node
        self.tail = node
        self.tail.prev = oldTail
        self.tail.next = None
        if prevNode is not None:
            prevNode.next = nextNode
        if nextNode is not None:
            nextNode.prev = prevNode
        if self.head == node:
            self.head = nextNode
            self.head.prev = None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        maxValue = 0
        currentNode = self.head
        while currentNode:
            if currentNode.value > maxValue:
                maxValue = currentNode.value
            currentNode = currentNode.next
        return maxValue
