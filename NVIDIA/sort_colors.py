from collections import Counter
from itertools import repeat


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []
        count = Counter(nums)
        for key, values in count.items():
            for i in range(values):
                ans.append(key)


        nums = sorted(ans)
        print(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.sortColors(nums = [2,0,2,1,1,0]))

