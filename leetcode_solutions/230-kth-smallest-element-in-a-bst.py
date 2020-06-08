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
            seen = []
            while root or len(stack) > 0:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    node = stack.pop()
                    seen.append(node.val)
                    root = node.right
                
            seen.sort()
            print("result is {}".format(seen))
            return seen[k-1]
            
