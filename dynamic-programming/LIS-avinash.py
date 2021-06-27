def lengthOfLIS(nums) -> int:
    def lengthOfLIS(self, nums) -> int:

        min = -100000000000  # some large negative integer

        def helper(nums, i, maxi, count):

            if i == len(nums):
                return 0

            if nums[i] > maxi:
                return max(1 + helper(nums, i + 1, nums[i], count + 1),
                           helper(nums, i + 1, maxi, count))
            else:
                return max(helper(nums, i + 1, min, 0) - count,
                           helper(nums, i + 1, maxi, count))

        return helper(nums, 0, min, 0)


if __name__ == '__main__':
    # print(lengthOfLIS([3, 10, 2, 1, 20]))
    # print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
    # print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
    print(lengthOfLIS([4, 10, 5, 4, 3]))
