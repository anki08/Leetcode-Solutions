class Solution:
    def subsets(self, nums):
        ans = []
        def subsets_util(start, end, output):
            ans.append(output[:])
            for i in range(start, end):
                output.append(nums[i])
                subsets_util(i+1,end, output)
                output.pop()
        subsets_util(0,len(nums), [])
        return ans



if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets(nums = [1,2,3]))