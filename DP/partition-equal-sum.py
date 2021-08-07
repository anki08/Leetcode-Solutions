def canPartition(nums) -> bool:
    # nums = sorted(nums)
    total_sum = sum(nums)
    # print(total_sum)
    for i in range(len(nums)):
        for j in range(i):
            # print(nums[i], nums[j])
            print(nums[j:i])
            subset_sum = sum(nums[j:i])
            if (subset_sum == total_sum / 2):
                return True
    return False


if __name__ == '__main__':
    # print(canPartition(nums = [1,5,11,5]))
    # print(canPartition(nums = [1,2,3,5]))
    # print(canPartition(nums = [1,1,2,2]))
    print(canPartition(nums=[14, 9, 8, 4, 3, 2]))
