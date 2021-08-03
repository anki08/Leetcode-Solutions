class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.x = None
        self.y = None
        self.pred = None

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def swap(root):
            if root.left: swap(root.left)
            if root.val > self.pred:
                self.y = root
                if self.pred and self.x is None:
                    self.x = self.pred
                else:
                    return

            pred = root
            swap(root.right)

        swap(root)
        self.x, self.y = self.y, self.x
        return root
