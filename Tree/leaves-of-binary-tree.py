from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: TreeNode):
        res = []
        ord = defaultdict(list)
        def dfs(root, level):
            if root is None:
                return level

            left = dfs(root.left, level)
            right = dfs(root.right, level)
            level = max(left, right)
            ord[level].append(root.val)
            return level + 1

        dfs(root, 0)
        res.append(val for val in ord.values())
        print(res)
