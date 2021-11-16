class Solution:
    def verifyPreorder(self, preorder):
        stack = []
        inorder = []
        for pre in preorder:
            while stack and stack[-1]<pre:
                inorder.append(stack.pop())
            stack.append(pre)
        while stack:
            inorder.append(stack.pop())
        if inorder == sorted(inorder):
            return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.verifyPreorder(preorder = [5,2,1,3,6]))