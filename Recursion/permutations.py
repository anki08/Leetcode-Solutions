class Solution:
    def __init__(self):
        self.ans = []
    def permute(self, nums):

        def permute_util(start, end, output):
            if start == end:
                self.ans.append(output[:])
                return
            for i in range(start, end):
                output[start], output[i] = output[i], output[start]
                permute_util(start+1, end, output)
                output[start], output[i] = output[i], output[start]

        permute_util(0, len(nums), nums)
        print(self.ans)
if __name__ == '__main__':
    sol = Solution()
    (sol.permute([1,2,3]))

