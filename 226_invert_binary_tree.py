def switch_node(root: TreeNode) -> TreeNode:

    if root is None:
        return root
    else:
        if root.left is not None or root.right is not None:
            delta = root.left
            root.left = root.right
            root.right = delta
            switch_node(root.left)
            switch_node(root.right)
    return root

new_root = switch_node(root)
print(new_root)
return new_root
