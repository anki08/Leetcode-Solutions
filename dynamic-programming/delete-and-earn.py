import numpy as np
from collections import Counter
def deleteAndEarn(nums) -> int:
    include, exclude = 0,0
    prev = None
    count = Counter(nums)
    for i in sorted(count):
        if i-1 != prev:
            exclude, include = max(include, exclude), i * count[i]+max(include, exclude)
        else:
            exclude, include = max(include, exclude), i * count[i] + exclude
        prev = i
    return  max(include, exclude)


if __name__ == '__main__':
    nums = [3,3,3,4, 10, 10, 11,11]
    print(deleteAndEarn(nums))