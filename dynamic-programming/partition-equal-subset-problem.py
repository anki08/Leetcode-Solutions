import numpy as np
def canPartitionRec(nums) -> bool:

    def canPartitionUtil(nums, total_sum, n):
        if(total_sum == 0):
            return True
        if(n==0 or total_sum<0):
            return False
        return (canPartitionUtil(nums, total_sum - nums[n-1], n-1) or canPartitionUtil(nums, total_sum, n-1))


    total_sum = sum(nums)
    if(total_sum %2 != 0):
        return False
    return canPartitionUtil(nums, total_sum//2, len(nums)-1)

def canPartitionMem(nums):
    n = len(nums)
    total_sum = sum(nums)
    if(total_sum %2 != 0):
        return False
    total_sum = total_sum//2
    dp = np.full((201, 101), False)
    dp[0][0] = True

    def canPartitionUtil(nums, total_sum, n):
        if (total_sum == 0):
            return True
        if (n == 0 or total_sum < 0):
            return False
        if (dp[total_sum][n] == True):
            return dp[total_sum][n]
        dp[total_sum][n] = (canPartitionUtil(nums, total_sum - nums[n-1], n-1) or canPartitionUtil(nums, total_sum, n-1))
        return dp[total_sum][n]

    return canPartitionUtil(nums, total_sum, n-1)

def canPartitionTopDown(nums):
    n = len(nums)
    total_sum = sum(nums)
    if (total_sum % 2 != 0):
        return False
    subset_sum = total_sum // 2
    dp = np.full((n+1, subset_sum+1), False)
    for j in range(subset_sum+1):
        dp[0][j] = False
    for i in range(1, n+1):
        dp[i][0] = True
    # dp[0][0] = True
    #
    for i in range(1, n+1):
        curr = nums[i-1]
        for j in range(1, subset_sum+1):
            if(curr > j):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j - curr] or dp[i-1][j])
    print(dp)
    return dp[-1][-1]



if __name__ == '__main__':
    # print(canPartitionRec([1,5,11,5]))
    # print(canPartitionMem([1,5,11,5]))
    print(canPartitionTopDown([1,5,11,5]))
    print(canPartitionTopDown([1,2,5]))