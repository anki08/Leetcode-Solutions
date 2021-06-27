def minMoves(nums) -> int:
    count = 0
    nums = sorted(nums)
    for i in range(1, len(nums)):
        count += nums[i] - nums[0]
    return count


if __name__ == '__main__':
    print(minMoves([13, 18, 3, 10, 35, 68, 50, 20, 50]))
