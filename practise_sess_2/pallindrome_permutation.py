from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        n = len(s)
        if n%2 == 1:
            c_1= 0
            for key, values in count.items():
                if values%2 != 0:
                    c_1 +=1
            if c_1>1:
                return False
        elif n%2 == 0:
            for key, values in count.items():
                if values%2 != 0:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPermutePalindrome("code"))
    print(sol.canPermutePalindrome("aab"))