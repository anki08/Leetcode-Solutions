from collections import Counter


class Solution:
    def findPairs(self, nums, k):
        left = 0
        right = 1
        result = 0
        while left < len(nums) and right < len(nums):
            if left == right or nums[right] - nums[left] <k:
                right +=1
            elif left == right or nums[right] - nums[left] >k:
                left +=1
            else:
                result+=1
                left += 1
                while nums[left-1]-nums[left] == k:
                    left+=1

        return (result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPairs(nums=[3, 1, 4, 1, 5], k=2))
    print(sol.findPairs(nums=[1, 2, 3, 4, 5], k=1))
    print(sol.findPairs(nums=[1, 3, 1, 5, 5, 4], k=0))
    print(sol.findPairs(nums=[1, 1, 1, 1, 1], k=0))
    print(sol.findPairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3))
    print(sol.findPairs(nums=[-1, -2, -3], k=1))
