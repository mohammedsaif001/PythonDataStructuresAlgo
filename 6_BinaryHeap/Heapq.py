import heapq

list1 = [10, 1, 65, 78, 654, 203, 456, 50]
print("Normal List", list1)

# heapifying the list
heapq.heapify(list1)
print("List after heapifying", list1)

# Root Node -> list1[1]
# Parent Node -> (i-1)//2
# Left Child -> (2*i)+1
# Right Child -> (2*i)+2

# Adding Additional value
heapq.heappush(list1, 25)
print("List after adding node: 25", list1)

# Deleting Root Node
heapq.heappop(list1)
print("List after Deleting the Root Node", list1)

# Insert an element then pops the root node and returns the deleted node
heapq.heappushpop(list1, 15)
print("Inserting 7 and deleting the root", list1)

# Pops the root/smallest node and returns it then it adds thengiven node. Also returns the deleted node
heapq.heapreplace(list1, 45)
print("Deleting root first and adding 45", list1)

# Getting n smallest nodes
minValues = heapq.nsmallest(3, list1)
print("3 Smallest values are ", minValues)

# Getting n Largest nodes
maxValues = heapq.nlargest(2, list1)
print("2 largest values are ", maxValues)
