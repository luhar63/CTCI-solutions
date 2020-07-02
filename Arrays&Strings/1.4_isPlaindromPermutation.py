"""
Palindrome permutation

"""


"""
Time Complexity: O(N)
Space Complexity: O(N)
"""


def getIndex(c):
    return ord(c) - ord("a")


def isPalindromePermutation(string):
    count_map = [0] * 26
    for c in string:
        if c == " ":
            continue

        c = c.lower()
        if count_map[getIndex(c)] == 0:
            count_map[getIndex(c)] += 1
        else:
            count_map[getIndex(c)] -= 1
    count_odd = 0
    for n in count_map:
        if n == 1:
            count_odd += 1
    return count_odd <= 1


# Driver Code
if __name__ == "__main__":
    string = "Tact Coa"
    print(isPalindromePermutation(string))
