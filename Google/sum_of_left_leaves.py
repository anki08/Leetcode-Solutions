# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        left_sum = 0
        def sum_func(node, is_left):
            nonlocal left_sum

            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.val if is_left == True else 0
            left_sum += sum_func(node.left, True)
            left_sum += sum_func(node.right, False)


        sum_func(root, False)
        return left_sum




