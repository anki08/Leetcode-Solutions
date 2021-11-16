# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        count = 0
        def util(root, max_val):
            nonlocal count
            if root is None:
                return
            count = 0
            left = util(root.left, root.val)
            right = util(root.right, root.val)
            if root.val > max_val:
                count += 1
                return count
            return left + right

if __name__ == '__main__':
    sol = Solution()
    sol.goodNodes([3,1,4,3,None,1,5])