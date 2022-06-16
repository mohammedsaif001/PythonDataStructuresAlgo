from collections import deque
queue = deque()

# Insertion
queue.append(10)
print(queue)
queue.append(40)
print(queue)
queue.append(50)
print(queue)
queue.append(60)
print(queue)

# Deletion
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
