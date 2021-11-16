class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start + end // 2
            if target == nums[mid]:
                return mid
            if nums[mid]>nums[start]:
                if target>nums[start] and target<nums[end]:
                    end = mid


if __name__ == '__main__':
    sol = Solution()
    print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))