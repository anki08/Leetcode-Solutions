class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):

        def get_paths(node, remaining_sum, res, path):
            if node is None:
                return False
            path.append(node.val)

            if remaining_sum == node.val and node.left is None and node.right is None:
                res.append(path)
            else:
                get_paths(node.left, remaining_sum - node.val, res, path)
                get_paths(node.right, remaining_sum - node.val, res, path)

            path.pop()
        res = []
        path = []
        get_paths(root, targetSum, res, path)
        return res

