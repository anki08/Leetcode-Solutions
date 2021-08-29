class Solution:
    def subarraySum(self, nums, k):
        curr_sum = 0
        hash_map = {}
        count = 0
        hash_map[0] = 1
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum-k in hash_map:
                count += hash_map[curr_sum-k]
            if curr_sum in hash_map:
                hash_map[curr_sum] += 1
            else:
                hash_map[curr_sum] = 1
        return count



if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraySum(nums = [1,1,1], k = 2))
    # print(sol.subarraySum(nums = [1,2,3], k = 3))
    # print(sol.subarraySum(nums=[1, -1, 0], k=0))