from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        queue = deque()
        ans = []
        queue.append(root)
        level = 0
        while len(queue)>0:
            ans.append([])
            while len(queue) > 0:
                node = queue.popleft()
                ans[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1



if __name__ == '__main__':
    sol = Solution()