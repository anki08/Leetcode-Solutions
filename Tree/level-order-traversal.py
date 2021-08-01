from collections import defaultdict, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        queue = deque()
        queue.append([root.val])
        level = 0
        res = []
        while queue:
            level +=1
            arr = []
            level_queue = deque()
            while len(queue)> 0:
                node = queue.popleft()
                arr.append(node.val)
                level_queue.append(node.left, node.right)
            res.append(arr)
            queue = level_queue
        print(res)






