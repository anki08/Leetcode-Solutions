class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.memo = {0:[], 1:[TreeNode(0)]}
    def allPossibleFBT(self, n: int):

        if n not in self.memo:
            ans = []
            for x in range(n):
                y = n-1-x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        fbt = TreeNode(0)
                        fbt.left = left
                        fbt.right = right

                        ans.append(fbt)
                self.memo[n] = ans
        return self.memo[n]



