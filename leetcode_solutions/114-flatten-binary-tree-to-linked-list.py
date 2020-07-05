# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        else:
            stack = []            
            last = TreeNode(-1)
            stack.append(root)
            while stack:
                node = stack.pop()
                last.right = node
                last.left = None
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                last = node
                
                
                
                
