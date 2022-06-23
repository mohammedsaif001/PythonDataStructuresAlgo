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


root = BinarySearchTree(None)
