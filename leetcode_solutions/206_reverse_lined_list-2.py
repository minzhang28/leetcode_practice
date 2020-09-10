# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head :
            return None
        elif not head.next:
            return head
        else:
            pre = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = pre
                
                pre = curr
                curr = nxt
            
        return pre
                
                
