class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def traversal(root, subroot):
            if subRoot is None:
                return True

            if root is None:
                return False

            if isIdentical(root, subRoot):
                return True

            return traversal(root.left, subRoot.left) or traversal(root.right, subRoot.right)

        def isIdentical(root, subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return  False
            return root.val == subRoot.val and  isIdentical(root.left, subRoot.left) and  isIdentical(root.right, subRoot.right)

        return traversal(root, subRoot)

