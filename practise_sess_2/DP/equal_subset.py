import numpy as np
class Solution:
    def canPartition(self, nums):
        nums = np.array(nums)
        total_sum = sum(nums)
        if total_sum%2 != 0:
            return False
        subset_sum = total_sum//2
        def can_partition_util(input, n, subset_sum):
            if subset_sum == 0:
                return True
            elif subset_sum<=0 or n==0:
                return False
            return can_partition_util(input, n-1, subset_sum-input[n-1]) or can_partition_util(input, n-1, subset_sum)

        return can_partition_util(nums, len(nums), subset_sum)




if __name__ == '__main__':
    sol = Solution()
    # print(sol.canPartition([1,5,11,5]))
    print(sol.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))
    # print(sol.canPartition( [1,2,3,5]))