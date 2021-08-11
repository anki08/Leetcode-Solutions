class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def solve(n, k):
            if n==1 and k==1:
                return 0
            mid = pow(2, n-1)/2

            if k <= mid:
                return solve(n-1, k)
            elif k> mid:
                return solve(n-1, k-mid) ^ 1

        print(solve(n,k))


if __name__ == '__main__':
    sol = Solution()
    sol.kthGrammar(3,4)