# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        result = root.val
        returnVal = True
        def getSub(root: TreeNode, result) -> bool:
            
            if root:
                if root.val == result:
                    r1 = getSub(root.left, result)
                    r2 = getSub(root.right, result)
                    return r1 and r2
                else:
                    return False
            else:
                return True
                    
        return getSub(root, result)
                
                        
