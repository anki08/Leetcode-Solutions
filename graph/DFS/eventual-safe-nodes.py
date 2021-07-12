import numpy as np
def eventualSafeNodes(graph):
    n = len(graph)
    visited = np.full(n+1, False)

    def dfs(graph, visited, node):
        if (len(graph) == 0 or node < 0 or node > len(node) - 1 or visited[node] == True):
            return

        if len(graph) > 0 and node > 0 and node < len(graph) and visited[node] != True:
            visited[node] = True
        for i in graph[node]:
            dfs(graph, visited, i)

    for i in graph[0]:
        dfs(graph, visited, i)
    print(visited[1:])


if __name__ == '__main__':
    print(eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
