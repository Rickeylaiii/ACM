#coding=gbk
def build_huffman_tree(nums):
    # ÿ���ڵ����ֵ��ʾ������ "weight", "left", "right", "height"
    nodes = []
    for num in nums:
        nodes.append({"weight": num, "left": None, "right": None, "height": 0})
    
    # �Զ���������򣺰� weight ���򣬵� weight ��ͬʱ�� height ����
    def node_key(node):
        return (node["weight"], node["height"])
    
    # �������������ÿ�κϲ�������С�ڵ�
    while len(nodes) > 1:
        nodes.sort(key=node_key)
        n1 = nodes.pop(0)
        n2 = nodes.pop(0)
        # �Ѿ�����n1["weight"] <= n2["weight"]
        # ��Ȩֵ���ʱ�������������֤ n1["height"] <= n2["height"],
        # �� n1 ��Ϊ���ӽڵ㣬n2 ��Ϊ���ӽڵ㣬������ĿҪ��
        new_node = {
            "weight": n1["weight"] + n2["weight"],
            "left": n1,
            "right": n2,
            "height": max(n1["height"], n2["height"]) + 1
        }
        nodes.append(new_node)
    return nodes[0]

def inorder_traversal(root):
    """��������������� -> ���ڵ� -> ������"""
    if root is None:
        return []
    return inorder_traversal(root["left"]) + [root["weight"]] + inorder_traversal(root["right"])

if __name__ == '__main__':
    # ��ȡ����
    n = int(input().strip())
    nums = list(map(int, input().split()))
    # �����������
    tree = build_huffman_tree(nums)
    # ����������ת��Ϊ�ַ�����Ȩֵ���Կո�ָ�
    result = inorder_traversal(tree)
    print(" ".join(map(str, result)))