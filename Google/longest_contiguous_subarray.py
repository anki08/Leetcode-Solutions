import numpy as np
class Solution:
    def longestSubarray(self, nums, limit):
        max_len =0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr = nums[i:j+1]
                min_e = np.min(arr)
                max_e = np.max(arr)
                # print(min_e, max_e)
                sub_sum = np.sum(nums[i:j+1])
                if max_e-min_e<=limit:
                    max_len=max(max_len, (j-i+1))
        return max_len



if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubarray(nums = [8,2,4,7], limit = 4))
    print(sol.longestSubarray(nums = [10,1,2,4,7,2], limit = 5))
    print(sol.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))
    print(sol.longestSubarray(nums = [8], limit = 10))