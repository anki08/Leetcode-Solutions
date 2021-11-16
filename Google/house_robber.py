import numpy as np
class Solution:
    def rob(self, nums) -> int:
        prev = None
        include, exclude = 0,0
        for i in nums:
            include, exclude = i+exclude, max(include, exclude)
        return max(include, exclude)

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([1,2,3,1]))
