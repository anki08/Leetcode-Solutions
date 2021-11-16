import heapq
class Solution:
    def findKthLargest(self, nums, k):
        return (heapq.nlargest(k, nums))[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))