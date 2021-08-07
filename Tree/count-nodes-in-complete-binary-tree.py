class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def depth(self, node):
        d = 0
        while(node.left):
            node = node.left
            d += 1
        return d

    def exists(self, index, d, node):
        left, right = 0, 2**d-1
        while left < right:
            pivot = left + (right-left) //2
            if index < pivot:
                node = node.left
                right  = pivot
            else:
                node = node.left
                left = pivot+1
        return node is None

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = self.depth(root)
        if d == 0:
            return 1

        left , right = 1, 2**d-1
        while left<right:
            pivot = left + (right-left) //2
            if self.exists(pivot, d, root):
                left = pivot +1
            else:
                right  = pivot -1

        return 2**d-1 + left

