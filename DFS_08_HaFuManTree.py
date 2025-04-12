#coding=gbk
def build_huffman_tree(nums):
    # 每个节点用字典表示，包含 "weight", "left", "right", "height"
    nodes = []
    for num in nums:
        nodes.append({"weight": num, "left": None, "right": None, "height": 0})
    
    # 自定义排序规则：按 weight 升序，当 weight 相同时按 height 升序
    def node_key(node):
        return (node["weight"], node["height"])
    
    # 构造哈夫曼树，每次合并两个最小节点
    while len(nodes) > 1:
        nodes.sort(key=node_key)
        n1 = nodes.pop(0)
        n2 = nodes.pop(0)
        # 已经排序，n1["weight"] <= n2["weight"]
        # 当权值相等时，由于排序规则保证 n1["height"] <= n2["height"],
        # 故 n1 作为左子节点，n2 作为右子节点，满足题目要求。
        new_node = {
            "weight": n1["weight"] + n2["weight"],
            "left": n1,
            "right": n2,
            "height": max(n1["height"], n2["height"]) + 1
        }
        nodes.append(new_node)
    return nodes[0]

def inorder_traversal(root):
    """中序遍历：左子树 -> 根节点 -> 右子树"""
    if root is None:
        return []
    return inorder_traversal(root["left"]) + [root["weight"]] + inorder_traversal(root["right"])

if __name__ == '__main__':
    # 读取输入
    n = int(input().strip())
    nums = list(map(int, input().split()))
    # 构造哈夫曼树
    tree = build_huffman_tree(nums)
    # 中序遍历结果转换为字符串，权值间以空格分隔
    result = inorder_traversal(tree)
    print(" ".join(map(str, result)))