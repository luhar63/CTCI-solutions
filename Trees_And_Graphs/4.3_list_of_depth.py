"""
List of Depths 
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def traverse(root):
    if root is None:
        return

    traverse(root.left)
    print(root.val, end=" ")
    traverse(root.right)


def listOfDepths(root):
    res = []
    if root is None:
        return res

    queue = []
    queue.append(root)
    while len(queue) > 0:
        size = len(queue)
        start = None
        current = None
        for i in range(size):
            last = queue.pop(0)
            if last.left is not None:
                queue.append(last.left)
            if last.right is not None:
                queue.append(last.right)
            if start is None:
                start = ListNode(last)
                current = start
                continue
            current.next = ListNode(last)
            current = current.next
        res.append(start)
    return res


def checkListOfDepth(lod):
    for i in range(len(lod)):
        start = lod[i]
        current = start
        print("level", i, end=" -> ")
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


def createTree(array):
    if len(array) == 0:
        return None
    root = TreeNode(array[0])
    queue = []
    queue.append(root)
    i = 1
    while i < len(array):
        node = queue[0]
        if array[i] is not None:
            if i % 2 == 1:
                node.left = TreeNode(array[i])
                queue.append(node.left)
            else:
                node.right = TreeNode(array[i])
                queue.append(node.right)
                queue.pop(0).val
        i += 1
    return root


# driver function
if __name__ == "__main__":
    array = [4, 5, 2, 1, 6, 3, 9, None, 7]
    root = createTree(array)
    print()
    checkListOfDepth(listOfDepths(root))
