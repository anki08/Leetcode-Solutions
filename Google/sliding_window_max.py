from collections import  deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        l = 0
        res = []
        max_q = deque()
        for r in range(len(nums)):
            while max_q and nums[max_q[-1]] < nums[r]:
                max_q.pop()
            max_q.append(r)
            max_e = nums[max_q[0]]
            if abs(r-l)==k-1:
                res.append(max_e)
                if max_q[0] == l:
                    max_q.pop()
                l+=1
        return res

if __name__ == '__main__':
    sol  = Solution()
    # print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(sol.maxSlidingWindow(nums = [7,2,4], k = 2))