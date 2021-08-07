class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def countNodes(self, root: TreeNode) -> int:

        def count(node):
            if node is None:
                return 0

            count(node.left)
            if node is not None:
                self.ans +=1
            count(node.right)

        count(root)
        return self.ans
