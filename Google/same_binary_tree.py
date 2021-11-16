# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        def util(p, r):
            if p is None and r is not None:
                return False
            if r is None and p is not None:
                return False
            if p is None and r is None:
                return True
            return p.val == p.val and util(p.left, r.left) and util(p.right, r.right)


if __name__ == '__main__':
    sol = Solution()