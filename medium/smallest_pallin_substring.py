class Solution:
    def longestPalindrome(self, s: str) -> str:
        string = s
        maxLength = 1

        start = 0
        length = len(string)

        low = 0
        high = 0

        for i in range(1, length):
            low = i - 1
            high = i
            while low >= 0 and high < length and string[low] == string[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

            low = i - 1
            high = i + 1
            while low >= 0 and high < length and string[low] == string[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

        return maxLength

if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome("babad"))
    # print("******")
    print(s.longestPalindrome("bbbb"))
    # print(s.longestPalindrome("cwqbbdsfgvbfhngjmkl"))
    # print(s.longestPalindrome("a"))
    # print(s.longestPalindrome("ac"))