# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def isMirror(t1: TreeNode, t2:TreeNode) -> bool:
            if not t1 and not t2:
                return True
            if not (t1 and t2):
                return False
        
            r1 = t1.val == t2.val
            r2 = isMirror(t1.left, t2.right)
            r3 = isMirror(t1.right, t2.left)
            
            return r1 and r2 and r3
        
        if not root:
            return True
        else:
            return isMirror(root.left, root.right)
