from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            else:
                temp = stack.pop()
                if ch != temp:
                    stack.append(temp)
                    stack.append(ch)
        print(stack)
        return "".join(stack)


if __name__ == '__main__':
    sol  =Solution()
    print(sol.removeDuplicates("abbaca"))