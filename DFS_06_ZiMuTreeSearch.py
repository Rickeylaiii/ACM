def build_tree(postorder, inorder):
    if not postorder or not inorder:
        return None
    
    root = postorder[-1]
    root_index = inorder.index(root)
    
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]
    
    left_postorder = postorder[:len(left_inorder)]
    right_postorder = postorder[len(left_inorder):-1]
    return {
        'val': root,
        'left': build_tree(left_postorder, left_inorder),
        'right': build_tree(right_postorder, right_inorder)
    }

def level_order(root):
    if not root:
        return ""
    queue = [root]
    res = ''
    while queue:
        node = queue.pop(0)
        res += node['val']
        if node['left']:
            queue.append(node['left'])
        if node['right']:
            queue.append(node['right'])
    return res

if __name__ == '__main__':
    postorder, inorder = input().split()
    tree = build_tree(postorder, inorder)
    print(level_order(tree))