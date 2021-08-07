import numpy as np
def maxProduct(nums) -> int:
    curr_product_max, curr_product_min, res = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        temp = max(nums[i], curr_product_max*nums[i], curr_product_min*nums[i])
        curr_product_min = min(nums[i], curr_product_min*nums[i],  curr_product_max*nums[i])
        curr_product_max = temp
        res = max(res, curr_product_max)


    print(res)

if __name__ == '__main__':
    # maxProduct([2,3,-2,4])
    # maxProduct([-2,0,-1])
    # maxProduct([-2,3,-4])
    # maxProduct([-2,-3,-4])
    # maxProduct([0,2])
    # maxProduct([-4,-3,-2])
    maxProduct([-1,-2,-9,-6])