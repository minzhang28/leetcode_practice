# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        else:
#             fast = head.next
#             slow = head
            
#             while slow != fast :
#                 if not fast or not fast.next:
#                     return False
                
#                 slow = slow.next
#                 fast = fast.next.next
            
#             return True
            r = []
            while head:
                if head in r:
                    return True
                else:
                    r.append(head)
                
                head = head.next
            
            return False
                
