class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def inorder(node, k):
            if node is None:
                return 0
            k -= 1
            inorder(node.left, k)
            # print(node.val)
            if k==0:
                return node.val
            inorder(node.right, k)

        return inorder(root, k)


