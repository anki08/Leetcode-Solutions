import numpy as np


def productExceptSelf(nums):
    prod_left = np.ones(len(nums))
    prod_right = np.ones(len(nums))
    prod = np.zeros(len(nums))
    for i in range(1, len(nums)):
        prod_left[i] = int(prod_left[i - 1] * nums[i - 1])
    for i in range(len(nums) - 2, -1, -1):
        prod_right[i] = int(prod_right[i + 1] * nums[i + 1])
    for i in range(len(nums)):
        prod[i] = int(prod_right[i] * prod_left[i])

    return prod


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
