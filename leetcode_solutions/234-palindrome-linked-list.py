# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        else:
            a = []
            while head.next:
                a.append(head.val)
                head = head.next
            else:
                a.append(head.val)
            print("a is {}".format(a))
            result = True
            for i in range(len(a) - 1):
                
                if a[i] != a[len(a)-1 -i]:
                    return False
                    break
            return result
            
