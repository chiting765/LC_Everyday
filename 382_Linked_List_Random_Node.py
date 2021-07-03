# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.items = []
        while head:
            self.items.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        index = int(random.random() * len(self.items))
        return self.items[index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
