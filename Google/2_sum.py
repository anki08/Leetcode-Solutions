class Solution:
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums)
        first, last = 0, len(nums)-1
        while first < last:
            if sorted_nums[first] + sorted_nums[last] == target:
                print(f'{first}, {last}')
                break
            elif sorted_nums[first] + sorted_nums[last] > target:
                last -= 1
            elif sorted_nums[first] + sorted_nums[last] < target:
                first += 1

        return [nums.index(sorted_nums[first]), len(nums)- nums[::-1].index(sorted_nums[last])-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums = [3,3], target = 6))