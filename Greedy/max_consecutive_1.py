class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count, sum_1 = 0, 0
        for i in range(len(nums)):
            sum_1 = sum_1+nums[i] if nums[i] == 1 else 0
            count = max(count, sum_1)
        return (count)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))