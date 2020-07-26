"""
Three in One: Implement three stacks using single one dimension array
"""


class MultiStack:
    def __init__(self, size):
        self.stack = []
        self.size = [0] * size
        # self.maxSize = 5

    def getTop(self, stackNum):
        i = 0
        offset = 0
        while i <= stackNum:
            offset += self.size[i]
            i += 1
        return offset

    def checkStackNum(self, stackNum):
        if stackNum >= len(self.size):
            print("Error: wrong stack number")
            exit(0)

    def push(self, stackNum, val):
        self.checkStackNum(stackNum)
        offset = self.getTop(stackNum)
        # maxOffset += self.max

        self.size[stackNum] += 1
        self.stack.insert(offset, val)

    def peek(self, stackNum):
        self.checkStackNum(stackNum)
        offset = self.getTop(stackNum)
        return self.stack[offset - 1]

    def pop(self, stackNum):
        self.checkStackNum(stackNum)
        if self.isEmpty(stackNum):
            return (
                "Error: Can't perform the action. Stack "
                + str(stackNum + 1)
                + " is empty"
            )
        offset = self.getTop(stackNum)
        self.size[stackNum] -= 1
        return self.stack.pop(offset - 1)

    def isEmpty(self, stackNum):
        self.checkStackNum(stackNum)
        return self.size[stackNum] == 0


if __name__ == "__main__":
    ms = MultiStack(3)
    ms.push(1, 2)
    ms.push(1, 4)
    ms.push(0, 3)
    ms.push(0, 6)
    ms.push(1, 8)
    ms.push(2, 5)
    ms.push(1, 10)
    ms.push(0, 9)
    ms.push(2, 15)
    print(ms.pop(1))

    print(ms.peek(2))
    print(ms.pop(0))

    print(ms.isEmpty(2))
    print(ms.pop(2))
    print(ms.pop(2))
    print(ms.pop(2))
