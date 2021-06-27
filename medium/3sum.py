def threeSum(nums):
    nums = sorted(nums)
    # nums = list(set(nums))
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            k = len(nums) - 1
            j = i + 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if (sum > 0):
                    k -= 1
                elif (sum < 0):
                    j += 1
                elif (sum == 0):
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    # while j < k and nums[j] == nums[j - 1]:
                    #     j += 1
    return res


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    # print(threeSum([-1,0,1,2,-1,4]))
