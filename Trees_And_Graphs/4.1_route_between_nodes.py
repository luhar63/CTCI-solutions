"""
Route b/w nodes
"""


def routeBetweenNodes(numberOfNodes, adjacencyList, source, destination):
    if source == destination:
        return True
    queue = []
    visited = [0] * (numberOfNodes + 1)  # 0-unvisited, 1- visiting, 2 - visited

    queue.append(source)

    while len(queue) > 0:
        u = queue.pop(0)
        visited[u] = 1
        if u not in adjacencyList:
            continue
        for v in adjacencyList[u]:
            if visited[v] == 0:
                if v == destination:
                    return True
                else:
                    queue.append(v)
        visited[u] = 2
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
