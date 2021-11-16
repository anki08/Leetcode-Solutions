# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        self.hash = set()
        self.ans = []

        def util(node):
            if node is None:
                return
            path = "".join(root.val,util(root.left), util(root.right))
            if path in self.hash:
                self.ans.append(path)
            self.hash.add(path)



if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicateSubtrees([1,2,3,4,null,2,4,null,null,4]))
