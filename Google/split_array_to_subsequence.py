import heapq
from collections import defaultdict
class Solution:
    def isPossible(self, nums) -> bool:
        subseqs = defaultdict(list)  # dictionary of heaps
        num_less_3 = 0
        for v in nums:
            v1 = v - 1
            if len(subseqs[v1]) == 0:
                heapq.heappush(subseqs[v], (1, [v]))
                num_less_3 += 1
            else:
                slen, shortest = heapq.heappop(subseqs[v1])
                if slen == 2:
                    num_less_3 -= 1
                shortest.append(v)
                heapq.heappush(subseqs[v], (slen + 1, shortest))

        return num_less_3 == 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPossible([1,2,3,3,4,4,5,5]))
