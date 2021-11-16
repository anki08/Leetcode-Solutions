class Solution:
    def lengthOfLIS(self, nums):
        global maximum

        def length_of_LIS_util(nums, index):
            global maximum
            if index == 1:
                return 1
            max_ending_here = 1
            for i in range(1, index):
                res = length_of_LIS_util(nums, i)
                if nums[i - 1] < nums[index - 1] and res + 1 > max_ending_here:
                    max_ending_here = res + 1
            maximum = max(max_ending_here, maximum)
            return max_ending_here

        maximum = 1
        length_of_LIS_util(nums, len(nums))
        return maximum


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
