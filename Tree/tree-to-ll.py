class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pred = None
        def linkedlist(node):
            nonlocal pred
            if node is None:
                return
            if pred:
                pred.right = node
                pred.left = None

            pred = node
            if node.left : linkedlist(node.left)
            if node.right: linkedlist(node.right)

        linkedlist(root)
        return root