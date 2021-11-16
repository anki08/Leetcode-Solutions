class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for el in nums1:
            flag = False
            index = nums2.index(el)
            for j in range(index+1, len(nums2)):
                if nums2[j] > el:
                    ans.append(nums2[j])
                    flag = True
                    break
            if flag == False:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))