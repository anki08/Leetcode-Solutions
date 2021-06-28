import numpy as np
def combinationSum4(nums, target) -> int:
    nums = sorted(nums)
    n = len(nums)
    dp = np.zeros((target, n), dtype=int)
    for i in range(n):
        if(nums[i]<=target):
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    for i in range(target):
        if(nums[0]<=i):
            dp[i][0] = 1
        else:
            dp[i][0] = 0

    for i in range(1, target):
        # curr = nums[i]
        for j in range(1, n):
            curr = nums[j]
            if(curr <= i):
                dp[i][j] = dp[i-curr][j] + dp[i][j-1]+ dp[i-curr][j-1] + dp[i][j]
            else:
                dp[i][j] = dp[i][j-1] + dp[i][j]

    print(dp)






if __name__ == '__main__':
    print(combinationSum4(nums = [1,2,3], target = 4))
    # print(combinationSum4(nums = [9], target = 3))