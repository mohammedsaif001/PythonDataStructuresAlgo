from queue import PriorityQueue
pQueue = PriorityQueue()
pQueue.put(10)
pQueue.put(40)
pQueue.put(50)
pQueue.put(20)
pQueue.put(15)

print(pQueue.get())
print(pQueue.get())
print(pQueue.get())
print(pQueue.get())
print(pQueue.get())
