from collections import  Counter
class Solution:
    def deleteAndEarn(self, nums):
        include, exclude = 0, 0
        count = Counter(nums)
        nums = list(set(sorted(nums)))
        prev = None
        for i in nums:
            if i != prev:
                include, exclude = max(include, exclude)+i*count[i], max(include, exclude)
            else:
                include, exclude = exclude +i*count[i] ,  max(include, exclude)

            prev = i
        return max(include, exclude)

if __name__ == '__main__':
    sol = Solution()
    print(sol.deleteAndEarn([3,4,2]))
