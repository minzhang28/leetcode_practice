def max_cal(root:TreeNode, max_depth:int): 
    depth_left,depth_right,depth_bottom = 0,0,0
    if root.left is not None:
        depth_left = max_cal(root.left, max_depth + 1)
    if root.right is not None:
        depth_right = max_cal(root.right, max_depth +1)
    if root.right is None and root.left is None:
        depth_bottom = max_depth +1
    return_val = max(max(depth_left,depth_right),depth_bottom)
    return return_val

if root is None:
    return 0
else:
    max_depth = max_cal(root,0)
    return(max_depth)
