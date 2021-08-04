class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff, res = 0, 0
        def inorder(node):
            nonlocal diff, res
            if node is None:
                return None


            if node.val < target:
                if abs(target-node.val) < diff:
                    res = node.val
                    diff = abs(target-node.val)
                node.left = inorder(node.left)
            else:
                if abs(target-node.val) < diff:
                    res = node.val
                    diff = abs(target-node.val)
                node.right = inorder(node.right)

        inorder(root)
        return res