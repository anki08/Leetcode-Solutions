# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        def util(root):
            if root is None:
                return
            left = util(root.left)
            right = util(root.right)
            return  max(left, right) + 1
        return util(root)


if __name__ == '__main__':
    sol = Solution()
    sol.maxDepth([3,9,20,None,None,15,7])
