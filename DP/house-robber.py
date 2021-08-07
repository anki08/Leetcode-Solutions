def rob(nums) -> int:
    include,exclude= 0,0
    for i in range(len(nums)):
        exclude, include = max(include, exclude) , exclude + nums[i]
    return max(include, exclude)


if __name__ == '__main__':
    print(rob([2,3,2]))
    print(rob([1]))
    print(rob([1]))
    print(rob([2,7,9,3,1]))
