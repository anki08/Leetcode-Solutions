from statistics import mode


def findShortestSubArray(nums) -> int:
    hash_fr = {}
    for i in range(len(nums)):
        if nums[i] in hash_fr:
            hash_fr[nums[i]][2] = i
            hash_fr[nums[i]][0] += 1
        else:
            hash_fr[nums[i]] = [1, i, i]

    mode_n = mode(nums)
    mode_a = [x for x in nums if x == mode_n]
    freq = len(mode_a)
    # print(freq)
    min_sub = 50001
    for key, value in hash_fr.items():
        if (value[0] == freq):
            min_sub = min(min_sub, (value[2] - value[1] + 1))
    return min_sub

if __name__ == '__main__':
    arr = [1,2]
    print(findShortestSubArray(arr))
