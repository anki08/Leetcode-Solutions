class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        def path_sum(root, remaining_sum, path):
            if root is None:
                return False

            path.append(root.val)
            if(remaining_sum == root.val):
                self.res.append(path)
                print(self.res)

            else:
                path_sum(root.left, remaining_sum-root.val, path)
                path_sum(root.right, remaining_sum-root.val, path)

            path.pop()

        path_sum(root, targetSum, [])

