class Node:
    def __init__(self, data):
        self.data = data
        self.nRef = None
        self.pRef = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printForward(self):
        # Check if LL is Empty
        if self.head is None:
            print("Linked List is Empty")
            return
        # Traverse All the Nodes
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.nRef
        print()

    def printBackward(self):
        # Check if LL is Empty
        if self.head is None:
            print("Linked List is Empty")
            return
        # Traversing Until Last Node without printing data
        n = self.head
        while n.nRef is not None:
            n = n.nRef
        # Printing Data Backwards
        while n is not None:
            print(n.data, end=" ")
            n = n.pRef
        print()
