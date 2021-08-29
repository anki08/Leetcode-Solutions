import math
class Solution:
    def kClosest(self, points, k):
        points = sorted(points, key=lambda x:(x[0]*x[0] + x[1]*x[1]))
        return points[:k]

if __name__ == '__main__':
    sol = Solution()
    print(sol.kClosest(points = [[1,3],[-2,2]], k = 1))