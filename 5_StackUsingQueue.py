from queue import LifoQueue
stack = LifoQueue()
stack = LifoQueue(maxsize=5)

# Adding Element
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40)
stack.put_nowait(50)


# Throws Error when Stack is Full instead of waiting
# stack.put_nowait(30)

# Checking the size of Stack
print("Size ->", stack.qsize())

# Checking if Stack is Empty
print("Stack Empty ->", stack.empty())

# Checking if Stack is Full
print("Stack is Full ->", stack.full())


# Removing Element
removed = stack.get()
print("Removed ->", removed)


# Removing All Elements from Stack
stack.get_nowait()
stack.get_nowait()
stack.get_nowait()
stack.get_nowait()

# Throws Error when Stack is Empty instead of waiting when we use nowait()
# stack.get_nowait()
