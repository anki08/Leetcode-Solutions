import re
class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub(' +', ' ', s)
        s = s.lstrip()
        s = s.rstrip()
        words = s.split(" ")
        return (' '.join(words[::-1]))


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))
    print(sol.reverseWords("  Bob    Loves  Alice   "))