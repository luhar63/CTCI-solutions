"""
Route b/w nodes
"""


def routeBetweenNodes(numberOfNodes, adjacencyList, source, destination):
    queue = []
    visited = [False] * (numberOfNodes + 1)

    queue.append(source)

    while len(queue) > 0:
        u = queue.pop(0)
        visited[u] = True
        if u not in adjacencyList:
            continue
        for v in adjacencyList[u]:
            if v == destination:
                return True
            if not visited[v]:
                queue.append(v)
    return False


# driver function
if __name__ == "__main__":
    adjacencyList = {}
    adjacencyList[1] = [2, 4]
    adjacencyList[2] = [3, 4]
    adjacencyList[3] = [5]
    numberOfNodes = 5
    source = 1
    destination = 5
    print(routeBetweenNodes(numberOfNodes, adjacencyList, source, destination))
