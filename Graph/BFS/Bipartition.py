from collections import defaultdict, deque
import numpy as np
def possibleBipartition( n: int, dislikes) -> bool:
    graph = defaultdict(list)
    for i, j in dislikes:
        graph[i].append(j)
        graph[j].append(i)
    color = np.zeros(n+1, int)
    for i in range(1, n+1):
        if color[i] == 0:
            q = deque()
            q.append(i)
            color[i] = 1
            while(q):
                parent = q.popleft()
                for node in graph[parent]:
                    if(color[node] == color[parent]):
                        return False
                    if(color[node] == 0):
                        q.append(node)
                        color[node] = -color[parent]
    return True

if __name__ == '__main__':

    print(possibleBipartition(n = 4, dislikes = [[1,2],[1,3],[2,4]]))