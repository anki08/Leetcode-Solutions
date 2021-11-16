from collections import defaultdict, deque
import heapq
class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        subordinates = defaultdict(list)
        for i, v in enumerate(manager):
            subordinates[v].append((informTime[i], i))
        print(subordinates)

        pq = [(informTime[headID], headID)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            dist[node] = d
            for d2, sub in subordinates[node]:
                if sub not in dist:
                    heapq.heappush(pq, (d + d2, sub))
        return (max(dist.values()))

if __name__ == '__main__':
    sol = Solution()
    # print(sol.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))
    # print(sol.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))
    # print(sol.numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))
    print(sol.numOfMinutes(n = 15, headID = 0, manager = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], informTime = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
