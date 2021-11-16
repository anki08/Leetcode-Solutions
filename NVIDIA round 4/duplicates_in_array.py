from collections import defaultdict
class Solution:
    def findDuplicates(self, nums):
        map = set()
        ans = []
        for i in nums:
            if i in map:
                ans.append(i)
            else:
                map.add(i)
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
