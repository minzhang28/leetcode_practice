# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        seen = []
        while root or len(stack) > 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                seen.append(node.val)
                root = node.right
                
        treeNode = temp = TreeNode(-1)        
        for i in range(len(seen)):
            temp.right = TreeNode(seen[i])
            temp = temp.right
        return treeNode.right
