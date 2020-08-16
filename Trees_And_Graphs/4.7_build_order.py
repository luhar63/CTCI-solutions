"""
Build Order
"""

from collections import *


def buildOrder(n, dep):
    visited = [0] * n
    adjList = defaultdict(list)
    res = []
    for u, v in dep:
        adjList[u] = v

    def dfs(node):
        num = ord(node) - 97
        if visited[num] == 2:
            return True
        if visited[num] == 1:
            return False

        visited[num] = 1
        for v in adjList[node]:
            if not dfs(v):
                return False
        visited[num] = 2
        res.append(node)
        return True

    for i in range(n):
        ch = chr(97 + i)
        print(ch)
        if not dfs(ch):
            return False
    res.reverse()
    return res


# driver function
if __name__ == "__main__":
    numberOfProjects = 6
    dependecies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
    res = buildOrder(numberOfProjects, dependecies)
    if res:
        print(res)
    else:
        print("Error")
