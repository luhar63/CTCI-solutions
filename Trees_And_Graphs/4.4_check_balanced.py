"""
Check Balanced
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

    print(root.val, end=" ")
    traverse(root.left)
    traverse(root.right)


# way 1: change the class TreeNode to store the height of every node
# way 2: create a recursive function to calculate height and return multiple values (valid, height#)
# way 3 : implement way 2 with a single return value --- using negative height


"""
Implementing way 3
"""


def checkBalanced(root):
    def check(node):
        if node is None:
            return 0

        leftHeight = check(node.left)
        rightHeight = check(node.right)

        if leftHeight < 0 or rightHeight < 0:
            return -abs(abs(leftHeight) + abs(rightHeight) + 1)

        if abs(leftHeight - rightHeight) > 1:
            return -abs(leftHeight + rightHeight + 1)
        else:
            return leftHeight + rightHeight + 1

    return True if check(root) > 0 else False


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
    array = [4, 5, None, 3]
    root = createTree(array)
    print(checkBalanced(root))
