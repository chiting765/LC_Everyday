"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        first, last = None, None
        first, last = self.inOrder(root, first, last)
    
        last.right = first
        first.left = last
        return first
        
    def inOrder(self, node, first, last):
        if node:
            first, last = self.inOrder(node.left, first, last)
            
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            
            last = node
            first, last = self.inOrder(node.right, first, last)
        return first, last
