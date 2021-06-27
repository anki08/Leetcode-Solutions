def rob(nums) -> int:
    exclude, include = 0, 0
    if (len(nums) == 1):
        return nums[0]
    for i in range(1, len(nums)):
        exclude, include = max(include, exclude), nums[i] + exclude
    exclude2, include2 = 0, 0
    for i in range(len(nums) - 1):
        exclude2, include2 = max(include2, exclude2), nums[i] + exclude2

    return max(include, exclude, include2, exclude2)


if __name__ == '__main__':
    # print(rob([2,3,2]))
    print(rob([1]))
