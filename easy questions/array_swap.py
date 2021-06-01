
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    zero = 0

    for i in range(len(nums)):
        if (nums[i] != 0):
            nums[zero], nums[i] = nums[i], nums[zero]
            zero += 1
    return nums

if __name__ == '__main__':
    a = [0,1,0,3,12]
    print(moveZeroes(a))