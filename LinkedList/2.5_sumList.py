"""
Sum List
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Just like merge sort.

Time Complexity: O(N)
Space Complexity: O(1)
"""


def sumList(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    res = None
    cur_res = None
    carry = 0
    while head1 and head2:
        value = (head1.val + head2.val + carry) % 10
        carry = (head1.val + head2.val + carry) // 10
        if res is None:
            res = ListNode(value)
            cur_res = res
        else:
            cur_res.next = ListNode(value)
            cur_res = cur_res.next
        head1 = head1.next
        head2 = head2.next

    while head1:
        value = (head1.val + carry) % 10
        carry = (head1.val + carry) // 10
        cur_res.next = ListNode(value)
        cur_res = cur_res.next
        head1 = head1.next

    while head2:
        value = (head2.val + carry) % 10
        carry = (head2.val + carry) // 10
        cur_res.next = ListNode(value)
        cur_res = cur_res.next
        head2 = head2.next

    if carry:
        cur_res.next = ListNode(carry)

    return res


# driver function
if __name__ == "__main__":
    num1 = [4, 3, 5]
    num2 = [9, 1, 2]
    head1 = None
    head2 = None
    cur = None
    for v in num1:
        if not head1:
            head1 = ListNode(v)
            cur = head1
        else:
            n = ListNode(v)
            cur.next = n
            cur = cur.next
    for v in num2:
        if not head2:
            head2 = ListNode(v)
            cur = head2
        else:
            n = ListNode(v)
            cur.next = n
            cur = cur.next

    head = sumList(head1, head2)

    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next

    print(res)
