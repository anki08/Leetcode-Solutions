class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memo = {0: [], 1: [TreeNode(1)]}

    def generateTrees(self, n: int):

        def unique_bst(start, end):
            if start > end:
                return
            ans = []
            for i in range(start, end):
                x = i-1
                y = n-i
                for left in x:
                    for right in y:
                        bst = TreeNode(i)
                        bst.left = left
                        bst.right = right

                        ans.append(bst)
            self.memo[n] = ans

        unique_bst(0, n+1)
        return self.memo[n]
