class Solution:
    def longestPalindrome(self, s):
        # odd
        max_len = curr_len = 0
        # ans = ""
        for i in range(len(s)):
            start = end = i
            curr_len = 1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    curr_len += 1
                    if curr_len > max_len:
                        ans = s[start:end + 1]
                        max_len = curr_len
                    start -= 1
                    end += 1
                else:
                    break
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                start, end = i - 1, i
                curr_len = 2
                while start >= 0 and end < len(s):
                    if s[start] == s[end]:
                        curr_len += 1
                        if curr_len > max_len:
                            ans = s[start:end + 1]
                            max_len = curr_len
                        start -= 1
                        end += 1
                    else:
                        break
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("babad"))
    print(sol.longestPalindrome("cbbd"))
