class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def dfs(node):
            if node is None:
                return False
            if node.val ==  key:
                if node.right is None:
                    return node.left
            if node.left is None:
                return node.right
            if node.right and node.left:
                temp = node.right
                while temp.left: temp = temp.left
                node.val = temp.val
                node.right = self.deleteNode(node.right, node.val)

            if (root.val > key):
                node.left = dfs(node.left, node, "left")
            else:
                node.right  = dfs(node.right, node, "right")


        node = root
        dfs(node)
        return root


