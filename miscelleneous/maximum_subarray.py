class Solution:
    def maxSubArray(self, nums):
        curr_sum = max_sum = 0
        for i in range(len(nums)):
            curr_sum = max(curr_sum+nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))