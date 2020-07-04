# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root and not k:
            return False
        else:
            stack = []
            d = {}
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    node = stack.pop()
                    if k - node.val in d:
                        return True
                    else:
                        d[node.val] = node.val
                    root = node.right
            return False
