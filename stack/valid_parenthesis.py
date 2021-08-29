class Solution:
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)

            else:
                last_ch = stack.pop()
                if (ch == ')' and last_ch != '(') or (ch == '}' and last_ch != '{') or (ch == ']' and last_ch != '['):
                    return False
        if len(stack)>0:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid(")"))

