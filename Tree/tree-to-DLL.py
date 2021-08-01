class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.head = None
        self.tail = None
        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            node = root
            if self.head is None:
                self.head = root
            else:
                self.tail.next = node
                node.left = self.tail

            self.tail = node
            dfs(node.right)

        dfs(root)
        return self.head


