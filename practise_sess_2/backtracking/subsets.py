class Solution:
    def subsets(self, nums):
        ans = []
        def util(nums, start, end, output):
            ans.append(output[:])
            for i in range(start, end):
                output.append(nums[i])
                util(nums, i+1, end, output)
                output.pop()


        util(nums, 0, len(nums), [])
        print(ans)


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1,2,3]))