class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        else:
            while root:   
                if root.val > val :
                    root = root.left
                elif root.val < val :
                    root = root.right
                elif root.val == val:
                    return root
