class Solution:
    def removeElement(self, nums, val):
        i = -1
        for j in range(len(nums)):
            if nums[j] == val:
                i = j
            elif i!= -1 and j > i:
                nums[i] = nums[j]
                i+=1

        print(nums)
        print(i)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement(nums = [2, 3,2,2,3, 5], val = 3))