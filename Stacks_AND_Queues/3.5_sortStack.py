"""
Sort Stack
"""


class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, v):
        if len(self.stack) == self.capacity:
            print("Error")
            exit(0)
        self.stack.append(v)

    def pop(self):
        if len(self.stack) == 0:
            print("Error")
            exit(0)
        return self.stack.pop(-1)

    def isFull(self):
        return self.capacity == len(self.stack)

    def isEmpty(self):
        return 0 == len(self.stack)

    def getTop(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def sortStack(stack):
    tempStack = Stack(10)

    while stack.size() > 0:
        if tempStack.size() == 0 or tempStack.getTop() < stack.getTop():
            tempStack.push(stack.pop())
        else:
            top = stack.pop()
            size = 0
            while tempStack.size() > 0 and top < tempStack.getTop():
                stack.push(tempStack.pop())
                size += 1

            tempStack.push(top)
            while size > 0:
                tempStack.push(stack.pop())
                size -= 1

    while tempStack.size() > 0:
        stack.push(tempStack.pop())

    return stack


# driver function
if __name__ == "__main__":
    q = Stack(10)
    q.push(4)
    q.push(3)
    q.push(6)
    q.push(9)
    q.push(1)
    q.push(7)
    q = sortStack(q)
    print(q.stack)
