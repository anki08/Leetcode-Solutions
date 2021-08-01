class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def diameter(node):
            if node is None:
                return 0

            lheight = height(root.left)
            rheight = height(root.right)

            ldiameter = diameter(root.left)
            rdiameter = diameter(root.right)
            return max(lheight + rheight, max(ldiameter, rdiameter))

        return diameter(root)



