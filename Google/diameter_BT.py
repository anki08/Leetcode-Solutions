# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        def util(root):
            if root is None:
                return 0
            left = util(root.left)
            right = util(root.right)
            return left+right+1


if __name__ == '__main__':
    sol = Solution()

