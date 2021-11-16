from collections import deque
class Solution:
    def longestSubarray(self, nums, limit):
        max_queue = deque()
        min_queue = deque()
        l = 0
        max_length = 0
        for r in range(len(nums)):
            while max_queue and nums[max_queue[-1]]<nums[r]:
                max_queue.pop()

            max_queue.append(r)

            while min_queue and nums[min_queue[-1]]>nums[r]:
                min_queue.pop()

            min_queue.append(r)

            max_el = nums[max_queue[0]]
            min_el = nums[min_queue[0]]

            diff = abs(max_el-min_el)
            if diff <= limit:
                max_length = max(max_length, r-l+1)
            else:
                if l==max_queue[0]:
                    max_queue.popleft()
                if l==min_queue[0]:
                    min_queue.popleft()

                l+=1
        return max_length


if __name__ == '__main__':
    sol =  Solution()
    print(sol.longestSubarray(nums = [8,2,4,7], limit = 4))
    print(sol.longestSubarray(nums = [10,1,2,4,7,2], limit = 5))