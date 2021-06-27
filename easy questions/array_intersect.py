def intersect(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    res = []
    i, j = 0, 0
    while (i < len(nums1) and j < len(nums2)):
        if (nums1[i] == nums2[j]):
            res.append(nums1[i])
            i += 1
            j += 1
        elif (nums1[i] > nums2[j]):
            j += 1
        elif (nums1[i] < nums2[j]):
            i += 1

    return res


if __name__ == '__main__':
    a1 = [1, 2, 2, 1]
    a2 = [2, 2]
    print(intersect(a1, a2))
