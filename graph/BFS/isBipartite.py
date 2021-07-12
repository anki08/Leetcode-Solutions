import numpy as np
from collections import deque, defaultdict
def isBipartite(graph) -> bool:
    n = len(graph)
    color = np.zeros(n, int)
    for i in range(n):
        if(color[i] == 0):
            queue = deque()
            queue.append(i)
            color[i] = 1
            while(queue):
                curr = queue.popleft()
                for j in graph[curr]:
                    if(color[curr] == color[j]):
                        return False
                    if(color[j] == 0):
                        color[j]= -color[curr]
                        queue.append(j)
    return  True


if __name__ == '__main__':
    print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
    print(isBipartite([[1,3],[0,2],[1,3],[0,2]]))