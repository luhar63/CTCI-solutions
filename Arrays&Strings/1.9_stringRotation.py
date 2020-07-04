"""
String Rotation 
"""


"""
Time Complexity: O(MN)
Space Complexity: O(MN)
"""


def stringRotation(s1, s2):
    length = len(s1)
    if length == len(s2) and length > 0:
        s1s1 = s1 + s1

        return s1s1.find(s2) > -1
    return False


# Driver Code
if __name__ == "__main__":

    print(stringRotation("waterbottle", "erbottlewat"))
