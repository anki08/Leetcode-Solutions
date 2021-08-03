class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def delNodes(self, root: TreeNode, to_delete):
        to_delete = set(to_delete)
        if root.val not in to_delete:
            self.res.append(root)

        def dfs(node, to_delete):
            if node is None:
                return
            if node.val in to_delete:
                if (node.right is not None):
                    self.res.append(node.right)

                if (node.left is not None):
                    self.res.append(node.left)

                return None

            node.left = dfs(node.left, to_delete)
            node.right = dfs(node.right, to_delete)

            return node

        dfs(root, to_delete)
        if root.val not in to_delete:
            self.res.append(root)
        return self.res
