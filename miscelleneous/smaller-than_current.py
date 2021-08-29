class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_array = sorted(nums)
        ans = []
        for i in nums:
            ans.append(sorted_array.index(i))
        return ans


if __name__ == '__main__':
    sol = Solution()
    # print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))
    print(sol.smallerNumbersThanCurrent([7,7,7,7]))
    print(sol.smallerNumbersThanCurrent([1,1,7]))
