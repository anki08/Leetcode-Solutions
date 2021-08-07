import heapq
import numpy as np
from collections import defaultdict
def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    pq = [(0,k)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist : continue
        dist[node] = d
        for nei, d2 in graph[node]:
            heapq.heappush(pq, ((d+d2), nei))
    return max(dist.values()) if len(dist) == n else -1




if __name__ == '__main__':
    # print(networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
    # print(networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
    # print(networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
    # print(networkDelayTime([[1,2,1],[2,1,3]], 2,2))
    print(networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1))
