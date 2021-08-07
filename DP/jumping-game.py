import numpy as np
def jump(nums) -> int:
    jumps = np.full(len(nums), np.inf)
    jumps[0] = 0
    for i in range(len(nums)):
        for j in range(i, i+nums[i]):
            if (j < len(nums)):
                jumps[j] = min(jumps[j], nums[i]+1)
    jumps[-1]


if __name__ == '__main__':
    print(jump([2,3,1,1,4]))