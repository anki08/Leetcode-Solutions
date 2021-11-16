from collections import Counter
class Solution:
    def deleteAndEarn(self, nums):
        prev = None
        include, exclude = 0, 0
        count = Counter(nums)
        for val in sorted(count):
            if val-1 != prev:
                include, exclude = count[val]*val+max(include, exclude), max(include, exclude)
            else:
                include, exclude = (count[val]*val)+exclude,  max(include, exclude)
            prev = val
        return max(include, exclude)


if __name__ == '__main__':
    sol = Solution()
    print(sol.deleteAndEarn([3,4,2]))