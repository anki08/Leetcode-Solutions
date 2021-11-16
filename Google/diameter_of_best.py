# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        def height(root):
            if root is None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return max(rh,lh)+1
        def util(root):
            if root is None:
                return 0
            ldia = util(root.left)
            lheight = height(root.left)
            rdia = util(root.right)
            rheight = height(root.right)
            return max(lheight+rheight+1, max(ldia, rdia))

        return util(root)