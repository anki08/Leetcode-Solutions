import numpy as np
class Solution:
    def canPartition(self, nums):
        target_sum = sum(nums)
        if target_sum %2 != 0:
            return False
        subset_sum = target_sum//2
        def canPartitionUtil(nums, index, subset_sum):
            if subset_sum == 0:
                return True
            elif subset_sum<=0 or index ==0:
                return False
            return canPartitionUtil(nums, index-1, subset_sum-nums[index]) or canPartitionUtil(nums, index-1, subset_sum)

        return canPartitionUtil(nums, len(nums)-1, subset_sum)





if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([1,5,11,5]))
