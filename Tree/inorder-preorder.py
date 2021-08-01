# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def helper(start, end):
            nonlocal preorderIndex
            if start > end:
                return None
            root = TreeNode(preorder[preorderIndex])
            preorderIndex += 1

            root.left = helper(start, inorderHash[preorder[preorderIndex]]-1)
            root.right = helper(inorderHash[preorder[preorderIndex]]+1, end)

            return root


        inorderHash = {}
        preorderIndex = 0
        for i in range(len(inorder)):
            inorderHash[inorder[i]] = i

        return helper(0, len(inorder)-1)


