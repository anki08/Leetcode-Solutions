class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:

        def max_money(node):
            if node is None:
                return [0,0]
            left = max_money(node.left)
            right = max_money(node.right)
            not_rob = max(left[0]) + max(right[0])
            rob = node.val + left[1] + right[1]

            return [rob, not_rob]

        max_money(root)
