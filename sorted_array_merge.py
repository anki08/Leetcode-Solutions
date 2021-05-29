def merge(nums1, m: int, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_copy = nums1[:m]
    low1 = 0
    low2 = 0
    for i in range(m + n):
        if (low2 >= n or (low1 < m and nums1_copy[low1] <= nums2[low2])):
            nums1[i] = nums1_copy[low1]
            low1 += 1

        else:
            nums1[i] = nums2[low2]
            low2 += 1

    print(nums1)



if __name__ == '__main__':
    a1 = [1, 2, 3, 0, 0, 0]
    m = 3
    a2 = [2, 5, 6]
    n = 3
    merge(a1, m, a2, n)