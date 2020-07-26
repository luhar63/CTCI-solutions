"""
Stack Min: implement a stack with min function to find minimum in stack: min should be O(1)
"""


"""
Going to store the minimum of 'substack' -(itself and below)

Time Complexity: O(1)
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, v):
        if len(self.stack) == 0:
            self.stack.append((v, v))
            return
        _, minimum = self.stack[-1]
        if v <= minimum:
            self.stack.append((v, v))
        else:
            self.stack.append((v, minimum))

    def pop(self):
        if len(self.stack) == 0:
            return "Error"
        value, _ = self.stack.pop(-1)
        return value

    def min(self):
        if len(self.stack) == 0:
            return "Error"
        _, minimum = self.stack[-1]
        return minimum


if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(6)
    s.push(10)
    s.push(2)
    s.push(4)
    print(s.min())
    print(s.pop())

