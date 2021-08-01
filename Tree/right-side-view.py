from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode):
        queue = deque()
        queue.append(root, None)
        curr = root
        right = [root]
        while queue:
            prev, curr = curr , queue.popleft()
            while curr:
                if (curr.left):
                    queue.append(curr.left)
                if (curr.right):
                    queue.append(curr.right)

                prev, curr = curr, queue.popleft()

            right.append(prev.val)

            if queue:
                queue.append(None)
        return right



