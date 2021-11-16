class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n >2 and n%2!=0:
            return False
        if n==1:
            return True
        i = 1
        pow = 2
        while pow**i<n:
            if pow**i == n:
                return True
            # pow = pow**i
            i+=1
        if pow ** i == n:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(n=1))
    print(sol.isPowerOfTwo(n=16))
    print(sol.isPowerOfTwo(n=3))