# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        seen = []
        
        if root:
            stack.append(root)
        else:
            return None
        while len(stack) > 0:
            node = stack.pop()
            seen.insert(0, node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                    
        return seen
    
