class Solution:
    def subarraySum(self, nums, k):
        count  = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
                    # break
        print(count)



if __name__ == '__main__':
    sol = Solution()
    # sol.subarraySum(nums = [1,1,1], k = 2)
    # sol.subarraySum(nums = [1,2,3], k = 3)
    sol.subarraySum(nums = [1,-1,0], k = 0)
