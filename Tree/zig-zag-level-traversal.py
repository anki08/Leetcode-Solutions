from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        queue = deque()
        queue.append(root)
        res = []
        height = -1
        while queue:
            height += 1
            level = []
            q2 = deque()
            while len(queue) > 0:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            if height % 2 == 1:
                res.append(level.reverse())
            else:
                res.append(level)
            queue = q2


        print(res)
