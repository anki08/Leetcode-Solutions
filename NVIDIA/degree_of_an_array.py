import statistics
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums):
        nums_mode = Counter(nums)
        freq = 0
        for key, values in nums_mode.items():
            freq = max(values, freq)
        min_space = 50001
        for key, values in nums_mode.items():
            if values == freq:
                space = (len(nums) - nums[::-1].index(key)) - nums.index(key)
                min_space = min(space, min_space)
        return min_space


if __name__ == '__main__':
    sol = Solution()
    print(sol.findShortestSubArray([1, 2, 2, 3, 1]))
    print(sol.findShortestSubArray([1,2,2,3,1,4,2]))
