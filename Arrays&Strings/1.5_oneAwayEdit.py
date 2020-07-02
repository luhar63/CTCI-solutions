"""
One Away Edit
"""


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""


def isOneAways(str1, str2):
    m = len(str1)
    n = len(str2)
    if abs(m - n) > 1:
        return False
    edits = 0
    big, small = (str1, str2) if m > n else (str2, str1)
    m = len(big)
    n = len(small)
    i1, i2 = 0, 0
    while i1 < m and i2 < n:
        if big[i1] != small[i2]:
            edits += 1
            if m == n:
                i2 += 1
        else:
            i2 += 1
        i1 += 1
        if edits > 1:
            return False
    return True


# Driver Code
if __name__ == "__main__":
    string = "pale"
    string2 = "pal"
    print(isOneAways(string, string2))
