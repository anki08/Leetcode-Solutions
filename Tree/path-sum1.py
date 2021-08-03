class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None and targetSum > 0:
            return False

        def dfs(root, targetSum):
            targetSum -= root.val

            if (root.left is None  and root.right is None):
                return targetSum == 0
            return dfs(root.left, targetSum) or dfs(root.right, targetSum)

        return dfs(root, targetSum)



