class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.postIndex = 0
        self.preIndex = 0

    def constructFromPrePost(self, preorder, postorder) -> TreeNode:


        def constructTree():
            node = TreeNode(preorder[self.preIndex])
            self.preIndex += 1

            if node.val != postorder[self.postIndex]:
                node.left = constructTree()
            if node.val != postorder[self.postIndex]:
                node.right = constructTree()
            self.postIndex += 1

            return node

        return constructTree()


