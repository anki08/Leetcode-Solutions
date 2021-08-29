class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parenthesis = []
        index = []
        for i in range(len(s)):
            if s[i].isalpha():
                continue
            if s[i] == ')' and len(parenthesis) == 0:
                index.append(i)
            elif s[i] == '(':
                parenthesis.append(i)
            elif s[i] == ')' and len(parenthesis) > 0:
                parenthesis.pop()

        for br in parenthesis:
            index.append(br)

        print(parenthesis)
        print(index)
        ans = [s[x] for x in range(len(s)) if x not in index]
        return "".join(ans)

if __name__ == '__main__':
    sol = Solution()
    # print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(sol.minRemoveToMakeValid("))(("))