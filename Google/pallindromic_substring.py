class Solution:
    def subsets(self, nums):
        substrings = []
        def util(sub, start, end):
            substrings.append(sub[:])
            for i in range(start, end):
                sub.append(nums[i])
                util(sub, i+1, end)
                sub.pop()
        util([], 0, len(nums))
        return substrings





if __name__ == '__main__':
    sol = Solution()
    # print(sol.countSubstrings("abc"))
    print(sol.subsets([1,2,3]))