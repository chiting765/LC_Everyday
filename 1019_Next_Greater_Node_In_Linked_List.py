# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        values.reverse()
        max_stack = []
        result = []
      
        for i, v in enumerate(values):
            while max_stack and v >= max_stack[-1]:
                max_stack.pop()
                
            if not max_stack: 
                result = [0] + result
            else:
                result = [max_stack[-1]] + result
                
            max_stack.append(v)
        
        return result  
