# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        temp = head
        prev = None
        while temp is not None:
            temp.next = prev

            prev = temp

        return prev



if __name__ == '__main__':
    sol = Solution()
    sol.reverseList(head = [1,2,3,4,5])