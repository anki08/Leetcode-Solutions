class Solution:
    def maxSubArray(self, nums):
        current_max = nums[0]
        maximum_max = nums[0]
        for number in nums[1:]:
            current_max = max(number, current_max+number)
            maximum_max = max(maximum_max, current_max)
        print(maximum_max)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))