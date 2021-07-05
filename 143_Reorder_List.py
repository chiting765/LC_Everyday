# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is the middle point
        prev, cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        first, second = head, prev

        while second.next:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            first = tmp1
            second.next = first
            second = tmp2
