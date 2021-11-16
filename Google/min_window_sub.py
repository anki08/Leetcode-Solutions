class Solution:
    def minWindow(self, s1: str, s2: str) -> str:

        original_s = s1[:]
        prev = -1
        flag = False
        start, end = None, None
        for i, ch in enumerate(s2):
            if ch not in s1:
                return ""
            if len(s2) == 1:
                return s2
            index = s1.index(ch)
            s1 = s1[:index]+"5"+s1[index+1:]

            if ch == s2[0] and start is None:
                start = index
            elif ch == s2[len(s2)-1] and end is None:
                end = index
            if index < prev:
                flag = True
                break
            prev= index
        if flag == True:
            return ""
        else:
            return original_s[start:end+1]
if __name__ == '__main__':
    sol = Solution()
    # print(sol.minWindow(s1 = "abcdebdde", s2 = "bde"))
    # print(sol.minWindow(s1 = "cnhczmccqouqadqtmjjzl", s2 = "mm"))
    # print(sol.minWindow(s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "k"))
    print(sol.minWindow(s1 = "cnhczmccqouqadqtmjjzl", s2 = "dq"))