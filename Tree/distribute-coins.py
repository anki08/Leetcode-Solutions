class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans  += abs(left) + abs(right)
            return node.val + abs(left) + abs(right) - 1

        return dfs(root)
