from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        curr_length = 0
        char_set = deque()
        for ch in s:
            if ch not in char_set:
                char_set.append(ch)
                curr_length += 1
            else:
                max_length = max(curr_length, max_length)
                temp = char_set.popleft()
                while temp != ch:
                    temp = char_set.popleft()
                char_set.append(ch)
                curr_length = len(char_set)
        return max_length
if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("dvdf"))

