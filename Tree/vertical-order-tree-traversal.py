from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode):
        queue = deque()
        hashmap = defaultdict(list)
        queue.append((root, 0))
        while queue:
                node, hor = queue.popleft()
                hashmap[hor].append(node.val)
                if node.left is not None:
                    queue.append((node.left, hor-1))
                if node.right is not None:
                    queue.append((node.right, hor+1))

        print (hashmap)
        print( [hashmap[val] for val in sorted(hashmap.keys())])

