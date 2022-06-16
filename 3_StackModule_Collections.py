import collections
stack = collections.deque()
print(stack)

stack.append(10)
stack.append(40)
stack.append(50)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

# Gives Error as there is no element
# stack.pop()
# print(stack)

# To Check IF Stack is Empty, returns True
print(not stack)

# To check last element in the stack
stack.append(10)
stack.append(50)
stack.append(40)
print(stack[-1])
