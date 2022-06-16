stack = []


def push():
    if len(stack) == n:
        print("Stack is Full")
    else:
        element = int(input("Enter Element: "))
        stack.append(element)


def pop():
    if not stack:
        print("Stack is Empty")
    else:
        removedEle = stack.pop()
        print(removedEle, " is Removed")


def isEmpty():
    if (len(stack) == 0):
        print("Stack is Empty")
    else:
        print(f"Length of Stack is ", {len(stack)})


def peek():
    if not stack:
        print("Stack is Empty")
    else:
        print(stack[-1])


n = int(input("Enter the length of Stack: "))
while True:
    choice = int(input(
        "\nEnter your Choice:\n1.Push\t2.Pop\t3.Last Element in Stack\t4.Check Length of Stack\t5.Quit\n"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        isEmpty()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
