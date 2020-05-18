# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        seen = []
        
        def findSub(root:TreeNode) :
            if root:
                seen.append(root.val)
                findSub(root.left)
                findSub(root.right)
            else:
                return None

        findSub(root)
        print("seen size is {}".format(len(seen)))
        return len(set(seen)) == 1
                
