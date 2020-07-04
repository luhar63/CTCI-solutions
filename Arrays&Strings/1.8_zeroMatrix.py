"""
Zero Matrix 
"""


"""
Time Complexity: O(MN)
Space Complexity: O(MN)
"""


def zeroMatrix(matrix):
    M = len(matrix)
    if M == 0:
        return matrix
    N = len(matrix[0])
    zeroX = []
    zeroY = []
    for i in range(0, M):
        for j in range(0, N):
            if matrix[i][j] == 0:
                zeroX.append(i)
                zeroY.append(j)
    for i in range(0, len(zeroY)):
        for j in range(0, M):
            matrix[j][zeroY[i]] = 0
    for i in range(0, len(zeroX)):
        for j in range(0, N):
            matrix[zeroX[i]][j] = 0

    return matrix


# Driver Code
if __name__ == "__main__":
    M = 4
    N = 4
    matrix = []
    count = 1
    for i in range(0, M):
        inner = []
        for j in range(0, N):
            inner.append(count)
            count += 1
        matrix.append(inner)
    matrix[1][2] = 0
    matrix[2][1] = 0
    print(zeroMatrix(matrix))
