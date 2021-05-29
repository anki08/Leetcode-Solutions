def nextGreaterElement( nums1, nums2):
    res = []
    for i in nums1:
        index = nums2.index(i)
        seen = False
        for j in range(index, len(nums2)):
            if nums2[j] > i:
                res.append(nums2[j])
                seen = True
                break
        if(seen == False):
            res.append(-1)
    return res


if __name__ == '__main__':
    print(nextGreaterElement([4,1,2], [1,3,4,2,5,6]))