class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return None
        else:
            stack = []
            stack.append(root)
            seen = []
            while len(stack) > 0 :
                node = stack.pop()
                seen.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left :
                    stack.append(node.left)
        return seen
