# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  

        while len(lists) > 1:
            i = 0
            merged_list = []
            while i < len(lists) - 1:     
                merged_list.append(self.mergeTwoLists(lists[i],lists[i+1]))
                i += 2
                
            if i != len(lists):
                merged_list.append(lists[-1])
                                   
            lists = merged_list
        
        return lists[0] if len(lists) > 0 else None
    
    def mergeTwoLists(self, list1, list2) -> ListNode:
        head = ListNode(0)
        dummy = head
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
                head = head.next
            else:
                head.next = list2
                list2 = list2.next
                head = head.next
        
        if list1:
            head.next = list1
        
        if list2:
            head.next = list2
        
        return dummy.next
