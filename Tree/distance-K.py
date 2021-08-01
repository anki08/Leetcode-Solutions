from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        def dfs(node, par):
            if(node):
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)

        queue = deque()
        queue.append([(target, 0)])
        seen = {target}
        while queue:
            node, dist = queue.popleft()
            if(dist == k):
                return [node.val for node, dist in queue]

            for nei in node.left, node.right, node.par:
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist+1))
        return []










