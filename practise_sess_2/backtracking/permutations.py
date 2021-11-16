class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        ans = []
        backtrack(0, len(nums))
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1,2,3]))
