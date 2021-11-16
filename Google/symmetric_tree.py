# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def util(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!= q.val:
                return False
            return util(p.left, p.right)
        util(root.left, root.right)


if __name__ == '__main__':
    sol = Solution()
    sol.isSymmetric(root = [1,2,2,3,4,4,3])