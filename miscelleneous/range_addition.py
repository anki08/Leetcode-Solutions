class Solution:
    def maxCount(self, m, n, ops):
        if len(ops) == 0:
            return m*n
        row = sorted(ops, key=lambda x : x[0])
        col = sorted(ops, key=lambda x : x[1])
        return row[0][0] * col[0][1]



if __name__ == '__main__':
    sol = Solution()
    # print(sol.maxCount(m = 3, n = 3, ops = []))
    # print(sol.maxCount(m = 1, n = 1, ops = [[1,1]]))
    print(sol.maxCount(18, 3, [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]))
    # print(sol.maxCount(m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))
    # print(sol.maxCount(26, 17,[[20,10],[26,11],[2,11],[4,16],[2,3],[23,13],[7,15],[11,11],[25,13],[11,13],[13,11],[13,16],[26,17]]))