# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        else:
            stack = []
            seen = []
            stack.append(root)
            
            def getNode(stack: List[int]):
                level_stack = []
                level_seen = []
                if len(stack) == 0:
                    return None
                while len(stack) > 0:
                    node = stack.pop()
                    level_seen.append(node.val)                        
                    if node.left:
                        level_stack.insert(0, node.left)
                    if node.right:
                        level_stack.insert(0, node.right)        
                        
                seen.append(level_seen)                
                getNode(level_stack)
            getNode(stack)
            return seen
