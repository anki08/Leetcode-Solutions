class Solution:
    def maxSubArray(self, nums) -> int:
        curr = -float('inf')
        max_til = -float('inf')
        for i in range(len(nums)):
            curr = max(nums[i], curr+nums[i])
            max_til = max(max_til, curr)
        return max(max_til, curr)



if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))