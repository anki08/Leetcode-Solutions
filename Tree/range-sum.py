class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0

        def dfs(root):
            nonlocal sum

            dfs(root.left)
            node = root
            if (node.val >= low and node.val <= high):
                sum += node.val
            dfs(node.left)

        dfs(root)
        return sum
