"""
String Compression 
"""


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""


def stringCompression(str1):
    i = 0
    newS = ""
    while i < len(str1):
        c = str1[i]
        count = 1
        while (i + 1) < len(str1) and str1[i + 1] == str1[i]:
            i += 1
            count += 1
        newS = newS + c + str(count)
        i += 1
    return str1 if len(newS) >= len(str1) else newS


# Driver Code
if __name__ == "__main__":
    string = "aaabbbbccccc"
    print(stringCompression(string))
