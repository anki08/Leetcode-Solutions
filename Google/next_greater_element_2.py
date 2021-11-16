class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        ans = []
        for i in range(len(nums)-1, -1, -1):
            while len(stack)>0 and nums[i]>=stack[-1]:
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(nums[i])
        return ans[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([4, 5, 2, 25]))
    print(sol.nextGreaterElements([11, 13, 21, 3]))