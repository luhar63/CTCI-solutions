"""
Return Kth to Last
"""


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
First Idea: We have to find the length of the linked list 
            then traverse to L-K+1 length

Time Complexity: O(N)
Space Complexity: O(1)
"""


# def getKthLast(head, K):
#     curr = head
#     l = getLength(head)
#     i = 0
#     while curr:
#         i += 1
#         if i == l - K + 1:
#             return curr.val
#         curr = curr.next
#     return None


"""
Second Idea: We can run another pointer after K runs of first pointer

Time Complexity: O(N)
Space Complexity: O(1)
"""


def getKthLast(head, K):
    curr = head
    i = 0
    currentAfterK = head
    while i < K:
        if not curr:
            return None
        i += 1
        curr = curr.next

    while curr:
        currentAfterK = currentAfterK.next
        curr = curr.next

    return currentAfterK and currentAfterK.val


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

    # res = []
    # cur = head
    # while cur:
    #     res.append(cur.val)
    #     cur = cur.next

    print(getKthLast(head, 7))
