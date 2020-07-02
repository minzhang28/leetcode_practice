# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        else:            
            stack = []
            result = []
            inorder = float('-inf')
            while len(stack) > 0 or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    node = stack.pop()
                    if result:
                        if node.val <= max(result):
                            return False
                    # if node.val <= inorder:
                    #     return False
                    result.append(node.val)
                    inorder = node.val
                    root = node.right
            return True
