class Solution:
    def twoSum(self, nums, target):
        map = {}
        for index, number in enumerate(nums):
            if number in map:
                return [map[number], index]
            else:
                map[target-number] = index
        # return

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums = [2,7,11,15], target = 9))