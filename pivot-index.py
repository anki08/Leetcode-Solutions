def pivotIndex(nums):
    sum_left = 0
    sum_right = 0
    if (len(nums) == 0):
        return 0
    for i in range(len(nums)):
        sum_left = sum(nums[:i])
        sum_right = sum(nums[i+1:])
        if(sum_left == sum_right):
            return i
    return 0


if __name__ == '__main__':
    nums = [2,1,-1]
    print(pivotIndex(nums))
