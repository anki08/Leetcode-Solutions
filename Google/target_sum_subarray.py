
class Solution:
    def minSumOfLengths(self, arr, target):
        dic = {}
        sum_v =0
        dic[0] = -1
        for i in range(len(arr)):
            sum_v += arr[i]
            dic[sum_v] = i
        res, lsize = float('inf'),float('inf')

        s = 0
        for i, val in enumerate(arr):
            s += val
            if s - target in dic:
                lsize = min(i - dic[s - target], lsize)

            if s + target in dic and lsize != float('inf'):
                rsize = dic[s + target] - i
                res = min(res, lsize + rsize)

        return -1 if res == float('inf') else res

if __name__ == '__main__':
    sol = Solution()
    print(sol.minSumOfLengths([3,1,1,1,5,1,2,1], target = 3))
