# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        queue = []
        res = []
        queue.append(root)
        
        while queue:
            r = []
            nex = []
            for node in queue:
                r.append(node.val)
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)    
            res.append(sum(r)/len(r))
            queue = nex
        
        return res
