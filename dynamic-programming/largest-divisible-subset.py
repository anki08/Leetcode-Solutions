import numpy as np
from collections import defaultdict
def largestDivisibleSubset_(nums):
    nums = sorted(nums)
    dp = np.ones(len(nums), dtype=int)
    for i in range(len(nums)):
        for j in range(i):
            if((nums[i] %nums[j]==0 or nums[j]%nums[i]==0) and dp[i] < dp[j]+1):
                dp[i] = dp[j]+1
    max_length = max(dp)
    max_index = np.argmax(dp)
    print(max_index, max_length)
    ans = [nums[max_index]]
    max_length -=1
    for i in range(max_index-1, -1, -1):
        if(max_length == dp[i] and ans[-1]%nums[i]==0):
            ans.append(nums[i])
            max_length -=1
    return ans[::-1]

def largestDivisibleSubset(nums):
    dp = {-1: set()}

    for num in sorted(nums):
        dp[num] = max([dp[k] for k in dp if num % k == 0], key=len) | {num}

    return list(max(dp.values(), key=len))


if __name__ == '__main__':

    # print(largestDivisibleSubset([1,2,4,8]))
    # print(largestDivisibleSubset([5,9,18, 54, 90, 108, 180, 360, 540]))
    print(largestDivisibleSubset([4,8,10,240]))