def nextPermutation(nums):
    for i in range(len(nums) - 2, 0, -1):
        if (nums[i + 1] <= nums[i]):
            for j in range(i, len(nums)):
                if (nums[i - 1] < nums[j] and (
                        j == len(nums) - 1 or (nums[i - 1] > nums[j + 1] and j < len(nums) - 1))):
                    nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
                    break
            reverse(nums, i - 1)
            break
    print(nums)


def reverse(nums, start):
    i, j = start, len(nums) - 1
    while (i < j):
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


if __name__ == '__main__':
    # nextPermutation([1,5,8,4,7,6,5,3,1])
    nextPermutation([2, 3, 1])
