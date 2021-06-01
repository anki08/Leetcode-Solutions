def findDisappearedNumbers(nums):
    n = len(nums)

    nums = list(set(sorted(nums)))
    res = []
    for i in range(1, n + 1):
        if i not in nums:
            res.append(i)
    return res

def findDisappearedNumbers2(nums):
    nums = list(set(sorted(nums)))
    print(nums)
    res = []
    for i in range(len(nums)-1):
        if (nums[i+1]- nums[i] > 1):
            res.append()
    return res

if __name__ == '__main__':
    print(findDisappearedNumbers([1,1]))
    # print(findDisappearedNumbers2([4,3,2,7,8,2,3,1]))