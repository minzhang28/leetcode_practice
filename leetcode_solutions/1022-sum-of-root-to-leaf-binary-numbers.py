# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        
        def helper(root:TreeNode, res) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return 2 * res + root.val
            res = 2 * res + root.val
            
            return helper(root.left, res) + helper(root.right, res)
        
        return helper(root, 0)
