from queue import Queue
q = Queue(maxsize=5)

print("Empty->", q.empty())
q.put(10)
q.put(20)
q.put(30)
print('Queue Size->', q.qsize())
q.put(40)
q.put(50)

# Gives Error when queue is Full
# q.put_nowait(50)

print("Full->", q.full())

q.get()
q.get()
q.get()
q.get()
q.get_nowait()

# Gives Error when queue is empty
# q.get_nowait()
