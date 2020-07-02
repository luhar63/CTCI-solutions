"""
1.3 URLify:
"""

"""
Time complexity: O(N^2)
Space Complexity: O(1)
"""


def urlify(s, num):
    i = num - 1
    string = list(s)
    while i >= 0:
        if string[i] == " ":
            j = num - 1
            while j > i:
                string[j + 2] = string[j]
                j -= 1
            string[i] = "%"
            string[i + 1] = "2"
            string[i + 2] = "0"
            num = num + 2
        i -= 1
    return "".join(string)


# Driver Code
if __name__ == "__main__":
    string = "Mr John Smith    "
    num = 13
    print(urlify(string, num))
