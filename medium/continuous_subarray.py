def subarraySum_brute_force(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sum_k = 0
            for z in range(i, j):
                sum_k += nums[z]

            if (sum_k == k):
                print(i, j)
                count += 1

    return count


def subarraySum_currsum(nums, k):
    cumulative_sum = {}
    cumulative_sum[0] = 1
    count, sum = 0, 0
    for i in range(len(nums)):
        sum += nums[i]
        key = sum - k
        if (key in cumulative_sum):
            count += cumulative_sum[key]

        if (sum in cumulative_sum):
            cumulative_sum[sum] += 1
        else:
            cumulative_sum[sum] = 1

    return count


if __name__ == '__main__':
    print(subarraySum_currsum([1], 1))
    print(subarraySum_currsum([1, 1, 1], 2))
    print(subarraySum_currsum([1, 2, 3], 3))
    print(subarraySum_currsum([-1, -1, 1], 0))
    print(subarraySum_currsum([3, 4, 7, 2, -3, 1, 4, 2], 7))
