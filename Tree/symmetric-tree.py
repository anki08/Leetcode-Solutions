class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def dfs(left, right):
            if left is None and right is None:
                return True
            if right is None or left is None:
                return False

            return (left.val == right.val) and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)