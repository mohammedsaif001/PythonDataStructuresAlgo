# Creating a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Creating Linked Lsit after creating Node
class LinkedList:
    # Creating Empty Linked List by giving head as None
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.ref
            print()

    def insertBeginning(self, data):
        newNode = Node(data)    # Create new Node
        newNode.ref = self.head     # Change newNode's Link to head
        self.head = newNode     # Change Head pointer to newNode

    def insertEnd(self, data):
        newNode = Node(data)         # Create new Node

        # Checking if LinkedList is Empty, if yes adding it to first pos
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            # Traversing until node's next is not null
            while n.ref is not None:
                n = n.ref
            n.ref = newNode  # Changing null to new node

    def insertInBetween_AfterNode(self, data, x):
        # Traversing till we get the pos or X value
        n = self.head
        while n is not None:
            if x == n.data:  # Checking if data field is equal to x, if yes then we got the position so terminate the loop
                break
            else:
                n = n.ref

        if n is None:  # If we dont find x i.e n.ref is None last node
            print("Node is not Present in Linked List")

        else:
            newNode = Node(data)     # Create new Node
            newNode.ref = n.ref
            n.ref = newNode

    def insertInBetween_BeforeNode(self, data, x):

        # Checking if LL is empty
        if self.head is None:
            print("Linked List is Empty so cant insert before the given node")
            return
        # Check if we are inserting before 1st node
        if self.head.data == x:
            newNode = Node(data)
            newNode.ref = self.head
            self.head = newNode
            return
        # Inserting anywhere between before the given node
        # Traversing the whole LL till we find x
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:  # Checking the next's data with x if yes then breaking the loop
                break
            n = n.ref
        if n.ref is None:
            print("Node is not Found")
        else:
            # Creating a new Node
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode

    def insertEmpty(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            print("Linked List is Not Empty")


ll1 = LinkedList()

ll1.printLinkedList()

print("\nInsertion in Beginning")
ll1.insertBeginning(10)
ll1.printLinkedList()
ll1.insertBeginning(20)
ll1.printLinkedList()
ll1.insertBeginning(30)
ll1.printLinkedList()

print("\nInsertion at End")
ll1.insertEnd(40)
ll1.printLinkedList()
ll1.insertEnd(50)
ll1.printLinkedList()

print("\nInsertion in Between After given Node")
ll1.insertInBetween_AfterNode(100, 20)
ll1.printLinkedList()
ll1.insertInBetween_AfterNode(100, 550)
ll1.printLinkedList()

print("\nInsertion in Between Before given Node")
ll1.insertInBetween_BeforeNode(150, 100)
ll1.printLinkedList()
ll1.insertInBetween_BeforeNode(100, 7550)
ll1.printLinkedList()
