class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        # Checking if BST isempty where 'root' is the obkject passed to self
        if self.key is None:
            self.key = data
            return

        # If Value is less than Root Node
        if data < self.key:
            # If lchild contains address (having subtree)
            if self.leftChild:
                # Call insert function again until we dont find sub-tree and find proper value for the tree
                self.leftChild.insert(data)
            else:
                # Inserting Data in Left child
                self.leftChild = BinarySearchTree(data)

        # If Value is greater than Root Node
        elif data > self.key:
            # If rchild contains address (having subtree)
            if self.rightChild:
                # Call insert function again until we dont find sub-tree and find proper value for the tree
                self.rightChild.insert(data)
            else:
                # Inserting Data in Right child
                self.rightChild = BinarySearchTree(data)

        # Duplicate Values is being ignored
        else:
            return

    def search(self, data):
        # If BST is Empty
        if self.key is None:
            print("Binary Search Tree is Empty")
            return

        # If root Node is the data
        if self.key == data:
            print("Node is Found :)")
            return

        # If data is less than root node
        if data < self.key:
            # If Left Subtree is present search the node
            if self.leftChild:
                self.leftChild.search(data)
            else:
                print("Node is not present in the Tree :<")

        # If data is greatar than root node
        elif data > self.key:
            # If Right Subtree is present search the node
            if self.rightChild:
                self.rightChild.search(data)
            else:
                print("Node is not present in the Tree :<")

    def preOrderTraversal(self):
        if self.key is None:
            print("Binary Search Tree is Empty")
            return

        # Root -> Left SubTree -> Right SubTree

       # Printing Root
        print(self.key, end=" ")
        # Left Subtree
        if self.leftChild:
            self.leftChild.preOrderTraversal()
        # Right Subtree
        if self.rightChild:
            self.rightChild.preOrderTraversal()

    def inOrderTraversal(self):
        if self.key is None:
            print("Binary Search Tree is Empty")
            return

        # Root -> Left SubTree -> Right SubTree

        # Left Subtree
        if self.leftChild:
            self.leftChild.inOrderTraversal()
        # Printing Root
        print(self.key, end=" ")
        # Right Subtree
        if self.rightChild:
            self.rightChild.inOrderTraversal()

    def postOrderTraversal(self):
        if self.key is None:
            print("Binary Search Tree is Empty")
            return

        # Root -> Left SubTree -> Right SubTree

        # Left Subtree
        if self.leftChild:
            self.leftChild.postOrderTraversal()
        # Right Subtree
        if self.rightChild:
            self.rightChild.postOrderTraversal()
        # Printing Root
        print(self.key, end=" ")


root = BinarySearchTree(10)
list1 = [21, 10, 30, 5, 12, 25, 100, 3, 7]
for data in list1:
    root.insert(data)
root.search(34)

print("\nPre Order Traversal")
root.preOrderTraversal()

print("\nIn Order Traversal")
root.inOrderTraversal()

print("\nPost Order Traversal")
root.postOrderTraversal()
