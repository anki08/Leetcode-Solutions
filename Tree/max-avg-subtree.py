class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        map_count = {-1:0}
        map_val = {-1:0}

        def dfs(root):
            nonlocal map_count, map_val
            if root is None:
                return None
            dfs(root.left)
            dfs(root.right)
            if root.right is None and root.left is None:
                map_count[root.val] = 1
                map_val[root.val] = root.val
            else:
                right_val = root.right.val if root.right else -1
                left_val = root.left.val if root.left else -1
                map_count[root.val] = map_count[right_val] + map_count[left_val] + 1
                map_val[root.val] = map_val[right_val] + map_val[left_val] + root.val

        dfs(root)
        print(map_count)
        print(map_val)
        max_avg = 0
        for key, value in map_val.items():
            if key != -1:
                max_avg = max(max_avg, map_val[key]/map_count[key])
        return max_avg


