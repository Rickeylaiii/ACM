#coding=gbk
def parse_tree(s, i):
    """
    �ݹ���������������� (node, next_index)
    �ڵ�node�����ֵ��ʾ��{'val': �ַ�, 'left': ������, 'right': ������}
    """
    # s[i] ����Ϊ��ĸ����Ϊ��ǰ�ڵ�ֵ
    node = {'val': s[i], 'left': None, 'right': None}
    i += 1  # �ƶ�����һ���ַ�
    # �����һ���ַ�Ϊ '{' ˵�������ӽڵ�����
    if i < len(s) and s[i] == '{':
        i += 1  # ���� '{'
        # ��ǰ����Ϊ�ջ�������
        # ����һ���ַ�Ϊ ',' ��ʾ������Ϊ��
        if s[i] == ',':
            left = None
        # ������������������Ż������ţ������������
        elif s[i] != '}':
            left, i = parse_tree(s, i)
        else:
            left = None  # ֱ������ '}' ����û���ӽڵ�
        node['left'] = left
        # �ж��Ƿ��ж��ţ���ʾ����������
        if s[i] == ',':
            i += 1  # ��������
            # ������ź�ֱ������ '}' ��ʾ������Ϊ��
            if s[i] != '}':
                right, i = parse_tree(s, i)
            else:
                right = None
            node['right'] = right
        # ������������ '}'
        if s[i] == '}':
            i += 1
    return node, i

def inorder_traversal(root):
    """��������������� -> ���ڵ� -> ������"""
    if not root:
        return ""
    return inorder_traversal(root['left']) + root['val'] + inorder_traversal(root['right'])

if __name__ == '__main__':
    # ��ȡ�����ַ���
    s = input().strip()
    tree, _ = parse_tree(s, 0)
    print(inorder_traversal(tree))