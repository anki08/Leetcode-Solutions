# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1, root2):

        def is_similar(root1, root2):
            if root1 is None and root2 is None:
                return  True
            if root1 is None or root2 is None or root2.val != root1.val:
                return  False

            return root1.val == root2.val and (is_similar(root1.left, root2.left) and is_similar(root2.right, root1.right)) or (is_similar(root1.left, root2.right) and is_similar(root1.right, root2.left))

        return is_similar(root1, root2)


