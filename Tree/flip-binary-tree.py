class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.i = 0
        self.ans = []

    def flipMatchVoyage(self, root, voyage):
        def dfs(node):
            if node is None:
                return

            if node.val != voyage[self.i]:
                self.ans = [-1]
                return
            self.i += 1
            if self.i < len(voyage) and node.left.val != voyage[self.i]:
                self.ans.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.ans
