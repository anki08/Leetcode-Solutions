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
        level = 0
        queue.append(root.val)
        arr = []
        while len(queue)>0:
            l = len(queue)
            level += 1
            lev_ar = []
            for i in range(l):
                node = queue.popleft()
                if node is None:
                    continue
                lev_ar.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            arr.append(lev_ar)
        print(arr)



if __name__ == '__main__':
    sol = Solution()
    sol.levelOrder([3,9,20,None,None,15,7])