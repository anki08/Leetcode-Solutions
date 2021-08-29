class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:x[0])
        ans = []
        for i in range(0, len(intervals)):
            if i-1>=0 and ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
                continue

            ans.append(intervals[i])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge(intervals = [[1,4],[4,5]]))
    print(sol.merge(intervals = [[1,3]]))
    print(sol.merge(intervals = [[1,4],[2,3]]))
    print(sol.merge(intervals = [[1,10],[4,5],[6,7],[8,9]]))

