class Solution:
    def rangeBitwiseAnd(self, left, right):
        bitwise_and = left
        for i in range(left+1, right+1):
            bitwise_and &= i
        return bitwise_and


if __name__ == '__main__':
    sol = Solution()
    print(sol.rangeBitwiseAnd(left = 5, right = 7))
