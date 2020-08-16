"""
Build Order
"""

from collections import *


"""

    I. IN CASE OF PARENT LINK:
        1. solve like linked-list intersection
        2. using cover(root, q) : root node covers q
    II. WHEN PARENT LINK IS NOT PRESENT:
    Can be done in two ways:
        1. check if root covers  p and q before start checking for ancestor 
        2. keep if nodes are found in return value 
"""

"""
SOLVING WITHOUT PARENT LINK

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def traverse(root):
    if root is None:
        return

    print(root.val, end=" ")
    traverse(root.left)
    traverse(root.right)


def contains(root, p):
    if root is None:
        return False
    if root == p:
        return True
    return contains(root.left, p) or contains(root.right, p)


"""
# WAY 1
def lowestCommonAncestor(root, p, q):
    if not contains(root, p):
        print("Can't find LCA")
        return None
    if not contains(root, q):
        print("Can't find LCA")
        return None
    res = lca(root, p, q)
    if res:
        print(res.val)
    else:
        print("None")

def lca(root, p, q):

    if root is None:
        return None
    if root == p or root == q:
        return root

    leftSearch = lca(root.left, p, q)

    rightSearch = lca(root.right, p, q)
    if leftSearch is None and rightSearch is None:
        return None
    if leftSearch is None:
        return rightSearch
    if rightSearch is None:
        return leftSearch
    return root
"""


# WAY 2 - taken from CTCI book
def lowestCommonAncestor(root, p, q):
    res, found = lca(root, p, q)
    if found:
        print(res.val)
        return
    print("None")


def lca(root, p, q):

    if root is None:
        return (None, False)
    if root == p and root == q:
        return (root, True)

    leftNode, leftFound = lca(root.left, p, q)
    if leftFound:
        return (leftNode, leftFound)

    rightNode, rightFound = lca(root.right, p, q)
    if rightFound:
        return (rightNode, rightFound)

    if leftNode is not None and rightNode is not None:
        return (root, True)
    elif root == p or root == q:
        return (root, leftNode is not None or rightNode is not None)
    else:
        # when only one is found
        if leftNode is not None:
            return (leftNode, False)
        else:
            return (rightNode, False)


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
        if i % 2 == 0:
            queue.pop(0).val
        i += 1
    return root


def returnNode(root, val):
    if root is None:
        return

    if root.val == val:
        return root
    left = returnNode(root.left, val)
    if left:
        return left
    right = returnNode(root.right, val)
    if right:
        return right


# driver function
if __name__ == "__main__":
    array = [3, 1, 5, None, None, None, 8]
    root = createTree(array)
    p = returnNode(root, 5)
    q = returnNode(root, TreeNode(7))

    lowestCommonAncestor(root, p, q)
