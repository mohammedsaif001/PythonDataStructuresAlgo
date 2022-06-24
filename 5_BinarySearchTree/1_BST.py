def count(node):
    if node is None:
        return 0
    # Total Nodes = left node/s + right node/s + 1(root)
    return 1 + count(node.leftChild) + count(node.rightChild)


class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insertNode(self, data):
        # Checking if BST isempty where 'root' is the obkject passed to self
        if self.key is None:
            self.key = data
            return

        # If Value is less than Root Node
        if data < self.key:
            # If lchild contains address (having subtree)
            if self.leftChild:
                # Call insert function again until we dont find sub-tree and find proper value for the tree
                self.leftChild.insertNode(data)
            else:
                # Inserting Data in Left child
                self.leftChild = BinarySearchTree(data)

        # If Value is greater than Root Node
        elif data > self.key:
            # If rchild contains address (having subtree)
            if self.rightChild:
                # Call insert function again until we dont find sub-tree and find proper value for the tree
                self.rightChild.insertNode(data)
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

    def deleteNode(self, data, rootNode):
        # Check if BST is Empty
        if self.key is None:
            print("BST is Empty")
            return

        # If data is less than node value go to left subtree and find the position
        if data < self.key:
            # If left node/subtree is present
            if self.leftChild:
                self.leftChild = self.leftChild.deleteNode(data, rootNode)
            else:
                print("Node Not Found")

        # If data is more than node value go to right subtree and find the position
        elif data > self.key:
            # If right node/subtree is present
            if self.rightChild:
                self.rightChild = self.rightChild.deleteNode(data, rootNode)
            else:
                print("Node Not Found")

        # If data equals node value
        else:
            # Node may have 0,1, 2 subchilds

            # If node contains only right subchild or 0
            if self.leftChild is None:
                temp = self.rightChild  # Storing Right Node in Temp

                # If node is Root Node
                if self.key == rootNode:
                    self.key = temp
                    self.leftChild = temp.leftChild
                    self.rightChild = temp.rightChild
                    temp = None  # Deleting Right child after data is been copied

                # Other than Root Node
                self = None     # Deleting the Value
                return temp     # Connecting right node to parent node after deletion

            # If node contains only left subchild or 0
            if self.rightChild is None:
                temp = self.leftChild  # Storing Left Node in Temp

                # If node is Root Node
                if self.key == rootNode:
                    self.key = temp
                    self.leftChild = temp.leftChild
                    self.rightChild = temp.rightChild
                    temp = None  # Deleting left child after data is been copied

                # Other than Root Node

                self = None     # Deleting the Value
                return temp     # Connecting left node to parent node after deletion

            # If node contains both childs left & right
            # Either we can take largest value if left subtree or lowest value in right subtree

            # Choosing lowest value in right subtree
            node = self.rightChild
            while node.leftChild:
                node = node.leftChild  # Iterate until you find lowest val
            # Replace the node with lowest val
            self.key = node.key
            # Break the chain by deleting node
            self.rightChild = self.rightChild.deleteNode(node.key, rootNode)
        return self

    def minNode(self):
        if self.key is None:
            print("BST is empty")
            return
        while self.leftChild:
            self = self.leftChild
        print("Min Node is ", self.key)

    def maxNode(self):
        if self.key is None:
            print("BST is empty")
            return
        while self.rightChild:
            self = self.rightChild
        print("Max Node is ", self.key)


root = BinarySearchTree(10)
list1 = [10, 15, 13, 20]
for data in list1:
    root.insertNode(data)
root.search(34)

print("\nPre Order Traversal")
root.preOrderTraversal()

print("\nIn Order Traversal")
root.inOrderTraversal()

print("\nPost Order Traversal")
root.postOrderTraversal()

print()
if count(root) > 1:
    print("Deleteing Node")
    root.deleteNode(10, root.key)
    root.inOrderTraversal()
else:
    print("Can't delete as there is only 1 node")

print()
root.minNode()
print()
root.maxNode()
