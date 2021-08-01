#Definition for a binary tree node.
import numpy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0


        def dfs(node, max_value):
            nonlocal count
            if (node.val >= max_value):
                count += 1
            if (node.left):
                dfs(node.left, max(max_value, node.val))
            if (node.right):
                dfs(node.right, max(max_value, node.val))

        dfs(root, -float('INF'))
        print(count)




if __name__ == '__main__':
    sol = Solution()
    print(sol.goodNodes([3,1,4,3,None,1,5]))
