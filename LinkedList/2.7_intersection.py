"""
Intersection
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
find the length difference and then check for intersection

Time Complexity: O(N)
Space Complexity: O(1)
"""


def getIntersection(head1, head2):
    len1 = getLength(head1)
    len2 = getLength(head2)
    if len1 > len2:
        k = len1 - len2
        while head1 and k > 0:
            head1 = head1.next
            k -= 1
    else:
        k = len2 - len1
        while head2 and k > 0:
            head2 = head2.next
            k -= 1
    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next

    return None


# driver function
if __name__ == "__main__":
    num1 = [4, 3, 5, 7, 2, 3]
    num2 = [6, 7, 2, 3]
    head1 = None
    head2 = None
    cur = None
    commonNode = None
    commonIndex1 = 2
    for i in range(0, len(num1)):
        v = num1[i]
        if not head1:
            head1 = ListNode(v)
            cur = head1
        else:
            n = ListNode(v)
            cur.next = n
            if i == commonIndex1:
                commonNode = n
            cur = cur.next
    commonIndex2 = 1
    for i in range(0, len(num2)):
        if i == commonIndex2:
            cur.next = commonNode
            break
        if not head2:
            head2 = ListNode(v)
            cur = head2
        else:
            n = ListNode(v)
            cur.next = n
            cur = cur.next

    node = getIntersection(head1, head2)
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
