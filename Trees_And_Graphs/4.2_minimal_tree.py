"""
Route b/w nodes
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse(root):
    if root is None:
        return
    traverse(root.left)
    print(root.val, end=" ")
    traverse(root.right)


def minimalTree(nums):
    def partition(start, end, nums):
        print(start, end)
        if start >= end:
            return TreeNode(nums[start])
        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])
        root.left = partition(start, mid - 1, nums)
        root.right = partition(mid + 1, end, nums)
        return root

    return partition(0, len(nums) - 1, nums)


# driver function
if __name__ == "__main__":
    sortedArray = [1, 2, 3, 4, 5, 6, 7]
    traverse(minimalTree(sortedArray))
    print()
