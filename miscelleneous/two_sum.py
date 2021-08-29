class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if target-nums[i] not in map:
                map[nums[i]] = i
            else:
                return [map[target-nums[i]], i]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums = [2,7,11,15], target = 9))