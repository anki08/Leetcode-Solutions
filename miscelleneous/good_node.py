# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.count = 0
    def goodNodes(self, root: TreeNode) -> int:

        def good_nodes_util(node, max_value):
            if node is None:
                return
            good_nodes_util(node.left, max(max_value, node.val))
            good_nodes_util(node.right, max(max_value, node.val))

            if node.val > max_value:
                self.res.append(node.val)
                self.count += 1

        good_nodes_util(root, root.val)
        return self.count + 1


