class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sum_n = n*(n+1)//2
        return sum_n - sum(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber(nums = [0,1]))
    print(sol.missingNumber(nums = [3,0,1]))
    print(sol.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))

