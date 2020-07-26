"""
Stack of Plates: implement a class setOfStacks for this
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
        return len(self.stack) - 1


class setOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def getLastStack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]

    def getStack(self, index):
        if len(self.stacks) < index:
            return None
        return self.stacks[index]

    def showStacks(self):
        for stackObj in self.stacks:
            print(stackObj.stack)

    def push(self, val):
        last = self.getLastStack()
        if not last:
            self.stacks.append(Stack(self.capacity))
            last = self.stacks[-1]

        if last.isFull():
            self.stacks.append(Stack(self.capacity))
            last = self.stacks[-1]
        last.push(val)

    def pop(self):
        last = self.getLastStack()
        if not last:
            print("Error")
            exit(-1)

        last.pop()

        if last.isEmpty():
            self.stacks.pop(-1)

    def popAt(self, index):
        last = self.getStack(index)
        if not last:
            print("Either empty or no stack present at index:", index)
            exit(-1)

        last.pop()

        if last.isEmpty():
            self.stacks.pop(index)


# driver function
if __name__ == "__main__":
    ss = setOfStacks(5)

    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(6)
    ss.showStacks()
    ss.popAt(0)
    ss.popAt(1)
    ss.showStacks()
