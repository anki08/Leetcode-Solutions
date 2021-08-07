import collections
import heapq
def numOfMinutes( n, headID, manager, informTime) -> int:
    subordinates = collections.defaultdict(list)
    for i, v in enumerate(manager):
        subordinates[v].append((informTime[i], i))
    print(subordinates)

    pq = [(informTime[headID],headID)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        dist[node] = d
        for d2, sub in subordinates[node]:
            if sub not in dist:
                heapq.heappush(pq, (d+d2, sub))
    print(max(dist.values()))




if __name__ == '__main__':
    numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0])