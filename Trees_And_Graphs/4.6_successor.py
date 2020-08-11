"""
Successor
"""


class TreeNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self):
        return str(self.val)


def traverse(root):
    if root is None:
        return

    print(root.val, end=" ")
    traverse(root.left)
    traverse(root.right)


import math

#


def getSuccessor(root):
    if root.right:
        node = root.right
        while node.left is not None:
            node = node.left
        return node
    else:
        while root.parent and root == root.parent.right:
            root = root.parent
    return root.parent


def createTree(array, target):
    if len(array) == 0:
        return None
    root = TreeNode(array[0])
    queue = []
    returningNode = root
    queue.append(root)
    i = 1
    while i < len(array):
        node = queue[0]
        if array[i] is not None:
            if i % 2 == 1:
                node.left = TreeNode(array[i], node)
                queue.append(node.left)
            else:
                node.right = TreeNode(array[i], node)
                queue.append(node.right)

        if array[i] == target:
            if i % 2 == 1:
                returningNode = node.left
            else:
                returningNode = node.right
        if i % 2 == 0:
            queue.pop(0).val
        i += 1
    return (root, returningNode)


# driver function
if __name__ == "__main__":
    array = [20, 10, 30, 5, 15, 28, None, 3, 7, None, 17, None, 29]
    root, testNode = createTree(array, 28)
    successor = getSuccessor(testNode)
    if not successor:
        print("No sucessor")
    else:
        print(successor.val)
