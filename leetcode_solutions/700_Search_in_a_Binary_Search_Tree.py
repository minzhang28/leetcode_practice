# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        while root:
            if root.val == val:
                return root
            else:
                if root.val < val:
                    root = root.right
                else:
                    root = root.left
        else:
            return None
