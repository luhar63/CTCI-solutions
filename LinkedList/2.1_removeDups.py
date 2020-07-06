"""
Remove Duplicates
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""


def removedups(head):
    curr = head
    while curr is not None:
        cnext = curr.next
        prev = curr
        while cnext is not None:
            if curr.val == cnext.val:
                prev.next = cnext.next
                cnext = prev.next
            else:
                prev = cnext
                cnext = cnext.next
        curr = curr.next
    return head


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

    head = removedups(head)
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next

    print(res)
