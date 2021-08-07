from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque()
        queue.append((root, 0))
        save_lev = None
        record_level = -1
        while queue:
            level_queue = deque()

            while queue:
                node, level = queue.popleft()
                if node.val == x or node.val == y:
                    if record_level == -1:
                        record_level = level
                    return level == record_level
                if node is None:
                    continue
                if node.left:
                    level_queue.append((node.left, level+1))
                if node.right:
                    level_queue.append((node.right, level+1))

            queue = level_queue

