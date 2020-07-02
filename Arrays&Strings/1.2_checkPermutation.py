"""
1.2 Check Permutation
"""


"""
Solution 1: Using Hash table
Time complexity: O(N)
Space complexity: O(N)
"""


# def checkPermutation(str1, str2):
#     counter = {}
#     l1 = len(str1)
#     l2 = len(str2)
#     if l1 != l2:
#         return False
#     for i in range(0, l1):
#         if str1[i] not in counter:
#             counter[str1[i]] = 0
#         counter[str1[i]] += 1

#     for i in range(0, l2):
#         if str2[i] in counter:
#             counter[str2[i]] -= 1
#         else:
#             return False
#     for k, v in counter.items():
#         if v != 0:
#             return False

#     return True


"""
Solution 1: Sorting both string
Time complexity: O(N Log N)
Space complexity: O(1)
"""


def checkPermutation(str1, str2):
    counter = {}
    l1 = len(str1)
    l2 = len(str2)
    if l1 != l2:
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, l1):
        if str1[i] != str2[i]:
            return False

    return True


# Driver Code
if __name__ == "__main__":
    str1 = "test"
    str2 = "tset"
    print(checkPermutation(str1, str2))

