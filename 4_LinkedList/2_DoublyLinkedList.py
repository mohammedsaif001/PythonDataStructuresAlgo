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

    def insertEmpty(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            print("Linked List is Not Empty")

    def insertBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            prevNode = self.head    # PrevNode is Head/1st Node
            newNode.nRef = prevNode     # newNode nRef is pointing to 1st Node
            prevNode.pRef = newNode     # 1st Node Pre Link is pointing to newNode
            self.head = newNode     # Head is pointing to New Node

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            # Traversing till Last Node
            n = self.head
            while n.nRef is not None:
                n = n.nRef
            n.nRef = newNode  # Changing Last node ref to newNode
            newNode.pRef = n  # Changing newNode prev to LastNode/2nd Last

    def insertAfterNode(self, data, val):
        # Check if LL is Empty
        if self.head is None:
            print("Linked List is Empty, Can't add After Node")
        else:
            # Travering till Last Node
            n = self.head
            while n is not None:
                # Break Loop if Value is found
                if val == n.data:
                    break
                n = n.nRef
            # If Value is not found till last node
            if n is None:
                print("Value no found in Linked List")
            else:
                # If Found, Create Node
                newNode = Node(data)
                newNode.nRef = n.nRef   # Point NewNode's next to node's next
                newNode.pRef = n        # Point NewNode's prev to Node
                if n.nRef is not None:  # If value found is not in last node
                    n.nRef.pRef = newNode  # Change Node's next element's prev to newNode
                n.nRef = newNode  # Node's next to newNode

    def insertBeforeNode(self, data, val):
        # Check if LL is Empty
        if self.head is None:
            print("Linked List is Empty, Can't add After Node")
        else:
            # Travering till Last Node
            n = self.head
            while n is not None:
                # Break Loop if Value is found
                if val == n.data:
                    break
                n = n.nRef
            # If Value is not found till last node
            if n is None:
                print("Value no found in Linked List")
            else:
                newNode = Node(data)
                newNode.nRef = n
                newNode.pRef = n.pRef
                # Checking if its not first node
                if n.pRef is not None:
                    n.pRef.nRef = newNode
                else:  # If its first node change head
                    self.head = newNode
                n.pref = newNode


dl1 = DoublyLinkedList()

dl1.insertEmpty(10)
print("\nPrinting in Forward Direction")
dl1.printForward()
#print("\nPrinting in Backward Direction")
# dl1.printBackward()

dl1.insertBeginning(20)
print("\nPrinting in Forward Direction")
dl1.printForward()
#print("\nPrinting in Backward Direction")
# dl1.printBackward()
dl1.insertBeginning(30)
print("\nPrinting in Forward Direction")
dl1.printForward()
#print("\nPrinting in Backward Direction")
# dl1.printBackward()

dl1.insertEnd(200)
print("\nPrinting in Forward Direction")
dl1.printForward()
#print("\nPrinting in Backward Direction")
# dl1.printBackward()
dl1.insertEnd(300)
print("\nPrinting in Forward Direction")
dl1.printForward()
#print("\nPrinting in Backward Direction")
# dl1.printBackward()

dl1.insertAfterNode(350, 300)
print("\nPrinting in Forward Direction")
dl1.printForward()
dl1.insertAfterNode(350, 3000)
print("\nPrinting in Forward Direction")
dl1.printForward()

dl1.insertBeforeNode(750, 350)
print("\nPrinting in Forward Direction")
dl1.printForward()
dl1.insertBeforeNode(350, 30)
print("\nPrinting in Forward Direction")
dl1.printForward()
