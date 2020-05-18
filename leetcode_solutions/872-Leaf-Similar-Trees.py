# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        r1 = []
        r2 = []
        def isLeafSimilar(root:TreeNode, result: List[int]):
            if root:
                print("root is {}".format(root.val))
                if not root.left and not root.right:
                    result.append(root.val)
                else:
                    isLeafSimilar(root.left, result)
                    isLeafSimilar(root.right, result)
            else:
                return None
        
        if root1 and root2:
            isLeafSimilar(root1, r1)
            isLeafSimilar(root2, r2)
            return r1 == r2
        else:
            return False
