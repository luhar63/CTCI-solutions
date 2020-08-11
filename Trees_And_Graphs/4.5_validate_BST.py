"""
Validate BST
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


import math

# way 1: Inorder traversal -> (storing it in an array - optional) -> checking if arr[i-1] < arr[i]
# way 2: make a recursive call and keep a min and max value for every subtree


"""
Implementing way two
"""


def validateBST(root):
    def validate(node, min, max):
        if node is None:
            return True

        if node.val <= min or node.val > max:
            return False

        return validate(node.left, min, node.val) and validate(
            node.right, node.val, max
        )

    return validate(root, -math.inf, math.inf)


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


# driver function
if __name__ == "__main__":
    array = [20, 10, 30, 5, 15, None, None, 3, 7, None, 17]
    root = createTree(array)
    print(validateBST(root))
