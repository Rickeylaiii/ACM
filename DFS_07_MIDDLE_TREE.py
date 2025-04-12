#coding=gbk
def parse_tree(s, i):
    """
    递归解析二叉树，返回 (node, next_index)
    节点node采用字典表示：{'val': 字符, 'left': 左子树, 'right': 右子树}
    """
    # s[i] 必须为字母，作为当前节点值
    node = {'val': s[i], 'left': None, 'right': None}
    i += 1  # 移动到下一个字符
    # 如果下一个字符为 '{' 说明存在子节点描述
    if i < len(s) and s[i] == '{':
        i += 1  # 跳过 '{'
        # 当前可能为空或有子树
        # 若第一个字符为 ',' 表示左子树为空
        if s[i] == ',':
            left = None
        # 如果不是立即遇到逗号或右括号，则解析左子树
        elif s[i] != '}':
            left, i = parse_tree(s, i)
        else:
            left = None  # 直接遇到 '}' 代表没有子节点
        node['left'] = left
        # 判断是否有逗号，表示存在右子树
        if s[i] == ',':
            i += 1  # 跳过逗号
            # 如果逗号后直接遇到 '}' 表示右子树为空
            if s[i] != '}':
                right, i = parse_tree(s, i)
            else:
                right = None
            node['right'] = right
        # 跳过结束括号 '}'
        if s[i] == '}':
            i += 1
    return node, i

def inorder_traversal(root):
    """中序遍历：左子树 -> 根节点 -> 右子树"""
    if not root:
        return ""
    return inorder_traversal(root['left']) + root['val'] + inorder_traversal(root['right'])

if __name__ == '__main__':
    # 读取输入字符串
    s = input().strip()
    tree, _ = parse_tree(s, 0)
    print(inorder_traversal(tree))