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
            def getMax(root, depth) -> int:
                if not root:
                    return depth
                else:
                    return max(getMax(root.left, depth + 1),getMax(root.right, depth + 1))
            depth = getMax(root, 0)
        return depth
            
