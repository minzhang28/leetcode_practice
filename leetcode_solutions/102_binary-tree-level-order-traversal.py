# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        stack=[]
        seen = []
        
        if not root:
            return None
        else:
            stack.append(root)
        
        def getNodes(stack: List[int]):
            level_stack=[]
            level_seen = []
            
            if len(stack) == 0:
                return None
            
            while len(stack) > 0:
                node = stack.pop()
                level_seen.append(node.val)
                if node.left :
                    level_stack.insert(0,node.left)
                
                if node.right :
                    level_stack.insert(0,node.right)


            seen.append(level_seen)

            getNodes(level_stack)
        
        
        getNodes(stack)
        
        return seen
