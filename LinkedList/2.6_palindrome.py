"""
Palindrome
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
reverse and traverse to check if is same as original list

Time Complexity: O(N)
Space Complexity: O(1)
"""


def checkPalindrome(head):
    reverse = None
    current = head
    while current:
        temp = ListNode(current.val)
        temp.next = reverse
        reverse = temp
        current = current.next
    while head and reverse:
        if head.val != reverse.val:
            return False
        head = head.next
        reverse = reverse.next
    return True


# driver function
if __name__ == "__main__":
    ls = [1, 2, 3, 7, 3, 2, 1]
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

    # head = checkPalindrome(head)

    # res = []
    # cur = head
    # while cur:
    #     res.append(cur.val)
    #     cur = cur.next

    print(checkPalindrome(head))
