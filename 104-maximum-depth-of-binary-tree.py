# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        else:
            depth = 0
            
            def getMax(node: TreeNode, depth: int) -> int:
                if not node:
                    return depth
                else:
                    left_depth = getMax(node.left, depth + 1)
                    right_depth = getMax(node.right, depth + 1)
                return max(left_depth, right_depth)
            
            
            return getMax(root, depth)
