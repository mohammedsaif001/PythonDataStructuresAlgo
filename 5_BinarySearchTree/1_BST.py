class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


root = BinarySearchTree(10)
print(root.key)
print(root.leftChild)
print(root.rightChild)

root.leftChild = BinarySearchTree(5)
print(root.leftChild.key)
print(root.leftChild.leftChild)
print(root.leftChild.rightChild)

print(root.leftChild)
