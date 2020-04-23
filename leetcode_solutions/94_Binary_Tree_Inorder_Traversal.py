# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack = []
        seen = []
         
        while root or len(stack) > 0:
            
            if root :
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                seen.append(node.val)
                root = node.right
                
        return seen
