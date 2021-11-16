class Solution:
    def longestSubarray(self, nums, limit) -> int:
        ans = []
        def util(out, start, end):
            ans.append(out[:])
            for i in range(start, end):
                out.append(nums[i])
                util(out,i+1, end)
                out.pop()
        util([], 0, len(nums))
        ans = sorted(ans, key = lambda x:len(x), reverse= True)
        for sub in ans:
            min_val = min(sub)
            max_val = max(sub)
            min_diff = abs(max_val-min_val)
            if min_diff<=limit:
                return len(sub)

        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubarray([8,2,4,7], 4))