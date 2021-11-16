# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        sum_node = 0
        def util(node):
            nonlocal sum_node
            if node is None:
                return 0
            if node and node.val > low and node.val<high:
                sum_node += node.val
            elif node.val < low:
                util(node.right)
            elif node.val > high:
                util(node.left)

        util(root)
        return sum_node

if __name__ == '__main__':
    sol = Solution()
