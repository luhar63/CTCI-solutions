"""
Partition
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""

Created two different linked list one ->  small, other -> big
combine them after runner loop gets over

Time Complexity: O(N)
Space Complexity: O(1)
"""


# def partitionLinkedList(head, x):
#     cur = head
#     if not head:
#         return None
#     small_start = None
#     big_start = None
#     small = None
#     big = None
#     while cur:
#         if cur.val < x:
#             if not small:
#                 small = ListNode(cur.val)
#                 start = small
#             else:
#                 small.next = ListNode(cur.val)
#                 small = small.next
#         else:
#             if not big:
#                 big = ListNode(cur.val)
#                 big_start = big
#             else:
#                 big.next = ListNode(cur.val)
#                 big = big.next
#         cur = cur.next
#     small.next = big_start
#     big.next = None
#     return start


"""

Created two different linked list one ->  small, other -> big
combine them after runner loop gets over

Time Complexity: O(N)
Space Complexity: O(1)
"""


def appendTo(head, curr, target):
    if not head:
        curr = target
        head = curr
    else:
        curr.next = target
        curr = curr.next
    return head, curr


def partitionLinkedList(head, x):

    if not head:
        return None
    big_head = None
    big_cur = None
    cur = head
    prev = None

    while cur:
        if cur.val >= x:
            if cur == head:
                big_head, big_cur = appendTo(big_head, big_cur, head)
                head = head.next
                cur = head
            else:
                big_head, big_cur = appendTo(big_head, big_cur, cur)
                prev.next = cur.next
                cur = cur.next
        else:
            prev = cur
            cur = cur.next
    if prev:
        prev.next = big_head
    else:
        head = big_head
    big_cur.next = None
    return head


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

    head = partitionLinkedList(head, 5)

    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next

    print(res)
