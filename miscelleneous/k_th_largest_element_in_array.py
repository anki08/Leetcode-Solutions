import heapq


class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        for i in range(len(nums)- k + 1):
            temp = heapq.heappop(nums)
        return (temp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))