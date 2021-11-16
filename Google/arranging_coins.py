class Solution:
    def arrangeCoins(self, n: int) -> int:
        stairs = 1
        while n >= stairs:
            n = n - stairs
            stairs += 1
        return stairs-1




if __name__ == '__main__':
    sol = Solution()
    print(sol.arrangeCoins(5))
    print(sol.arrangeCoins(8))
