class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def dfs(root):
            if root is None:
                return 0

            return 1+ dfs(root.left) + dfs(root.right)
        return dfs(root)
