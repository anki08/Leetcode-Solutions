class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0
        for el in pushed:
            stack.append(el)
            while stack and stack[-1] == popped[j] :
                stack.pop()
                j+=1

        return len(stack) == 0



if __name__ == '__main__':
    sol = Solution()
    print(sol.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
    print(sol.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))