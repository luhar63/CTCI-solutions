"""
Rotate Matrix 
"""


"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""


def rotateMatrix(matrix):
    L = len(matrix)
    for i in range(0, L // 2):
        first = i
        last = L - 1 - i
        for j in range(first, last):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][L - 1 - i]
            matrix[j][L - 1 - i] = matrix[L - 1 - i][L - 1 - j]
            matrix[L - 1 - i][L - 1 - j] = matrix[L - 1 - j][i]
            matrix[L - 1 - j][i] = temp
    return matrix


# Driver Code
if __name__ == "__main__":
    L = 4
    matrix = []
    count = 1
    for i in range(0, L):
        inner = []
        for j in range(0, L):
            inner.append(count)
            count += 1
        matrix.append(inner)

    print(rotateMatrix(matrix))
