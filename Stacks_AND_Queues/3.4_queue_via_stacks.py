"""
Queue via Stacks: implementing a class myQueue using two stacks
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


class MyQueue:
    def __init__(self):
        self.stack1 = Stack(10)
        self.stack2 = Stack(10)

    def switchTo(self, stack1, stack2):
        if stack1.size() < stack2.size():
            while stack2.size() > 0:
                stack1.push(stack2.pop())

    def add(self, val):
        self.switchTo(self.stack1, self.stack2)
        self.stack1.push(val)

    def remove(self):
        if self.isEmpty():
            print("Empty")
            return None
        self.switchTo(self.stack2, self.stack1)
        return self.stack2.pop()

    def isEmpty(self):
        return max(self.stack1.size(), self.stack2.size()) == 0

    def peek(self):
        if self.isEmpty():
            print("Empty")
            return None
        self.switchTo(self.stack2, self.stack1)
        return self.stack2.getTop()


# driver function
if __name__ == "__main__":
    q = MyQueue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    print(q.remove())
    q.add(5)
    print(q.peek())
    print(q.remove())
    print(q.peek())
