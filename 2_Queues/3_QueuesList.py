queue = []


def enqueue():
    if isFull():
        print("Queue is Full -> OverFlow Condition")
    else:
        element = int(input('Enter the Element: '))
        queue.append(element)


def dequeue():
    if isEmpty():
        print("Queue is Empty -> UnderFlow Condition")
    else:
        queue.pop(0)


def isEmpty():
    if len(queue) == 0:
        return True
    else:
        return False


def isFull():
    if len(queue) == n:
        return True
    else:
        return False


def firstElement():
    if not isEmpty():
        First = queue[0]
        print("First Element ->", First)
    else:
        print("Queue is Empty")


def lastElement():
    if not isEmpty():
        Last = queue[-1]
        print('Rear ELement -> ', Last)
    else:
        print("Queue is Empty")


n = int(input("Enter the Size of Queue: "))
while True:
    choice = int(input(
        "\nEnter Your Choice\n1.Enqueue\t2.Dequeue\t3.UnderFlow\t4.OverFlow\t5.First Element\t6.Rear Element\t7.Quit\n"))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        print("Underflow", isEmpty())
    elif choice == 4:
        print("Overflow", isFull())
    elif choice == 5:
        firstElement()
    elif choice == 6:
        lastElement()
    elif choice == 7:
        break
    else:
        print("Invalid Choice :( ")
