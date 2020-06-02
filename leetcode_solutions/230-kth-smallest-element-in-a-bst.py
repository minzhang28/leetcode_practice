# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        if not root or not k:
            return None
        else:
            stack = []
            stack.append(root)
            result = []
            while len(stack) > 0:
                node = stack.pop()
                if node:
                    result.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            result.sort()
        return result[k-1]
