# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if not node:
            return None
        else:
            val = node.next.val
            node_next = node.next.next
            
            node.val = val
            node.next = node.next.next
