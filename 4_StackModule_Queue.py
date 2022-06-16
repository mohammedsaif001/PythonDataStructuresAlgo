import queue
stack = queue.LifoQueue()

# Adding Limit to Stack
stack = queue.LifoQueue(5)

# Adding Elements
stack.put(10)
stack.put(40)
stack.put(70)
stack.put(120)
stack.put(120)


# Timeout if stack is full
stack.put(120, timeout=1)


# Removing Elements
stack.get()
stack.get()
stack.get()
stack.get()
stack.get()

# Timeout if Stack is Empty
stack.get(timeout=1)
