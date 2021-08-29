class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==0:
            return True
        if n == 1:
            return True
        if n%2 !=0:
            return False
        return self.isPowerOfTwo(n//2)

if __name__ == '__main__':
    sol = Solution()
    # print(sol.isPowerOfTwo(n=1))
    print(sol.isPowerOfTwo(n=16))