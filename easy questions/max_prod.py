def maximumProduct(nums) -> int:
    nums = sorted(nums)
    print("1", nums[-1] * nums[-2] * nums[-3])
    print("2", nums[0] * nums[1] * nums[-1])
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[2] * nums[-1])

if __name__ == '__main__':
    arr = [-100,-98,-1,2,3,4]

    print(maximumProduct(arr))