"""
Loop Detection
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLength(root):
    length = 0
    while root:
        length += 1
        root = root.next
    return length


"""
slow and fast pointer ... runner pointer to look for cycle

Time Complexity: O(N)
Space Complexity: O(1)
"""


def loopDetection(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:  # no meeting poiont found.
        return None
    else:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

    return fast


# driver function
if __name__ == "__main__":
    num1 = [4, 3, 5, 7, 2, 3]
    head = None

    cur = None
    loopNode = None
    loopIndex = 2
    for i in range(0, len(num1)):
        v = num1[i]
        if not head:
            head = ListNode(v)
            cur = head
        else:
            n = ListNode(v)
            if i == loopIndex:
                loopNode = n
            if i == len(num1) - 1:
                n.next = loopNode

            cur.next = n
            cur = cur.next

    node = loopDetection(head)
    if node:
        print(node.val)
    else:
        print(node)

    # res = []
    # cur = head
    # while cur:
    #     res.append(cur.val)
    #     cur = cur.next

    # print(res)
