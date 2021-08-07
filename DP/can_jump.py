import numpy as np
def canJump(nums) -> bool:
    dp = np.full(len(nums), False)
    if(nums[0] == 0 and len(nums)> 1):
        return False
    elif(len(nums) == 1):
        return True

    dp[0] = True
    for i in range(len(nums)-1):

        for j in range(i, i+nums[i]+1):
            if(j < len(nums)):
                dp[j] = (dp[j]or dp[i])
    print (dp)
    return dp[-1]

if __name__ == '__main__':
    print(canJump([2,3,1,1,4]))
    print(canJump([3,2,1,0,4]))
    print(canJump([0]))
    print(canJump([1,0,1,0]))