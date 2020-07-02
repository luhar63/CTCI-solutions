"""
Is Unique
"""

"""
Solution 1:
time complexity: O(N^2)
space complexity : O(1)
"""


# def isUnique(string):
#     l = len(string)
#     for i in range(0, l):
#         for j in range(i + 1, l):
#             if string[i] == string[j]:
#                 return False
#     return True


# print(isUnique("Good Morning"))
# print(isUnique("Night"))

"""
Solution 2: sorting before traversal 
time complexity: O(N Log N)
space complexity : O(1)
"""


def isUnique(string):
    l = len(string)
    string = sorted(string)
    for i in range(1, l):
        if string[i - 1] == string[i]:
            return False
    return True


print(isUnique("Good Morning"))
print(isUnique("Night"))
