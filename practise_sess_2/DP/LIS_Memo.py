import numpy as np
class Solution:
    def lengthOfLIS(self, nums):
        global maximum
        dp = np.zeros(2500, dtype=int)
        dp[0] = 1
        dp[1] = 1

        def length_Of_LIS_util(index, nums):
            global maximum
            if dp[index] != 0 or index == 1:
                return dp[index]
            max_ending_here = 1
            for i in range(1, index):
                dp[i] = length_Of_LIS_util(i, nums)
                if nums[i-1]<nums[index-1] and dp[i]+1 > max_ending_here:
                    max_ending_here = dp[i] +1
            maximum = max(max_ending_here, maximum)
            return max_ending_here

        maximum =1
        length_Of_LIS_util(len(nums), nums)
        print(dp[len(nums)-1])
        return maximum

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))