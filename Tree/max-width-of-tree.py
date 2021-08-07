from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = deque()
        queue.append(root, 0)
        max_node = 0
        while queue:
            level_width = 0
            level_queue = deque()
            _, prev_level = queue[0]
            while queue:
                node, column_width = queue.popleft()
                if node and node.left:
                    level_queue.append(node.left, column_width*2)
                elif node and node.right:
                    level_queue.append(node.left, column_width*2+1)

            queue = level_queue
            max_node = max(max_node, level_width-prev_level)
        print(max_node)

