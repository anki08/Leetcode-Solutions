from collections import defaultdict, deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            level += 1
            level_queue = deque()
            node, prev = None, None
            while len(queue)> 0:
                node = queue.popleft()
                if node is None:
                    continue
                if prev: prev.next = node
                if node.left : level_queue.append(node.left)
                if node.right : level_queue.append(node.right)
                prev = node

            if node : node.next = None
            queue = level_queue

        return root

