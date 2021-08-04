class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        prev = None

        def inorder(root):
            nonlocal prev
            if root is None:
                return
            inorder(root.left)
            if prev:
                prev.right = root
                prev.left = None
            prev = root
            inorder(root.right)

        inorder(root)
        return root