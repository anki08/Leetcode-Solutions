class Solution:
    def subsetsWithDup(self, nums):
        substrings = []

        def util(sub, start, end):
            word = sub[:]
            if sorted(word) not in substrings:
                substrings.append(sorted(sub[:]))
            for i in range(start, end):
                sub.append(nums[i])
                util(sub, i + 1, end)
                sub.pop()

        util([], 0, len(nums))
        return substrings


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))