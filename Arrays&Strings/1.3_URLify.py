"""
1.3 URLify:
"""

"""
Time complexity: O(N^2)
Space Complexity: O(1)
"""


# def urlify(s, num):
#     i = num - 1
#     string = list(s)
#     while i >= 0:
#         if string[i] == " ":
#             j = num - 1
#             while j > i:
#                 string[j + 2] = string[j]
#                 j -= 1
#             string[i] = "%"
#             string[i + 1] = "2"
#             string[i + 2] = "0"
#             num = num + 2
#         i -= 1
#     return "".join(string)

"""
Time complexity: O(N)
Space Complexity: O(1)
"""


def urlify(s, length):
    string = list(s)
    count = 0

    for i in range(0, length):
        if string[i] == " ":
            count += 1
    index = length + (2 * count) - 1
    for i in range(length - 1, -1, -1):
        if string[i] == " ":
            string[index] = "0"
            string[index - 1] = "2"
            string[index - 2] = "%"
            index = index - 3
        else:
            string[index] = string[i]
            index -= 1
    return "".join(string)


# Driver Code
if __name__ == "__main__":
    string = "Mr John Smith    "
    num = 13
    print(urlify(string, num))
