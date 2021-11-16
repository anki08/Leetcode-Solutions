class Solution:
    def calculate(self, s):
        w = ""
        s = s.replace(" ","")
        stack = []
        res = 0
        op = "+"
        for i in range(len(s)+1):
            if i < len(s) and s[i].isdigit():
                w += s[i]
            else:
                if op == "+":
                    stack.append(w)
                elif op == "-":
                    stack.append("-"+w)
                elif op == "*":
                    stack.append(int(stack.pop())*int(w))
                elif op == "/":
                    stack.append(int(stack.pop())/int(w))
                if i < len(s):
                    op = s[i]
                else:
                    op = "+"
                w = ""

        while stack:
            res += int(stack.pop())
        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.calculate("3+2*2"))
    # print(sol.calculate(" 3/2 "))
    print(sol.calculate(" 3+5 / 2 "))
