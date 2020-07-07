"""
Delete the middle node
"""
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLength(head):
    length = 0
    while head:
        head = head.next
        length += 1
    return length


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""


def deleteMiddleNode(node):
    if not node or not node.next:
        return None
    node.val = node.next.val
    node.next = node.next.next


# driver function
if __name__ == "__main__":
    ls = [4, 3, 5, 6, 7, 3, 2, 1]
    head = None
    cur = None
    for v in ls:
        if not head:
            head = ListNode(v)
            cur = head
        else:
            n = ListNode(v)
            cur.next = n
            cur = cur.next

    num = random.randrange(1, len(ls) - 1)
    cur = head
    while num > 0:
        cur = cur.next
        num -= 1

    print("delete : ", cur.val)
    deleteMiddleNode(cur)

    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next

    print(res)
