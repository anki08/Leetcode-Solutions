class Solution:
    def removeDuplicates(self, nums):
        i, j, end = 1, 1, len(nums)-1
        while i <= len(nums)-1:
            if nums[i] == nums[i-1]:
                i += 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1,1,5, 5]))



