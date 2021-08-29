class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root, k) -> bool:
        node = root
        traversal = []

        def dfs(node):
            if node is None:
                return None

            dfs(node.left)
            traversal.append(node.val)
            dfs(node.right)

        dfs(node)
        start = 0
        end = len(traversal) - 1
        while start < end:
            sum = traversal[start] + traversal[end]
            if sum == k:
                print(True)
            elif sum > k:
                end -= 1
            else:
                start += 1

