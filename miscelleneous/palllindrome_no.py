class Solution:
    def isPalindrome(self, x: int) -> bool:
        input = [i for i in str(x)]
        copy = input[:]
        input.reverse()
        if copy == input:
            return True
        else:
            return False
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(121))