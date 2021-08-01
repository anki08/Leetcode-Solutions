class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root, par = None):
            if root is None:
                return
            root.parent = par
            if (root.left):
                dfs(root.left, root)
            if (root.right):
                dfs(root.right, root)

        dfs(root, None)
        p1, p2 = p,q
        while p1!= p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1



