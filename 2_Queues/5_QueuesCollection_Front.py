from collections import deque
queue = deque()

queue.appendleft(10)
print(queue)
queue.appendleft(20)
print(queue)
queue.appendleft(30)
print(queue)

queue.pop()
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)
