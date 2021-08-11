class Solution:
    def __init__(self):
        self.ans = []
    def subsets(self, nums):

        def subsets_util(nums, output, start, end):
            self.ans.append(output[:])
            for i in range(start, end):
                output.append(nums[i])
                subsets_util(nums, output, i+1, end)
                output.pop()

        subsets_util(nums, [], 0, len(nums))

if __name__ == '__main__':
    sol = Solution()
    sol.subsets([1,2,3])
    print(sol.ans)

