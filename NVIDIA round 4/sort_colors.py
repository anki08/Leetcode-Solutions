from collections import Counter
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = curr = 0
        end = len(nums)-1
        while curr<=end:
            if nums[curr] ==0:
                nums[start], nums[curr] = nums[curr], nums[start]
                start += 1
                curr +=1
            elif nums[curr] == 2:
                nums[curr], nums[end] = nums[end], nums[curr]
                end-=1
            else:
                curr+=1

        print(nums)

if __name__ == '__main__':
    sol = Solution()
    # print(sol.sortColors([2,0,2,1,1,0]))
    print(sol.sortColors([2,0, 1]))
    print(sol.sortColors([1,2,0]))