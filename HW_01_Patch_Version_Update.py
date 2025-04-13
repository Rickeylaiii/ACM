import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    n = int(data[0])
    # 存储当前补丁的前序版本，若前序版本为NA，则用None处理
    parent_map = {}
    # 记录所有出现的当前补丁版本和作为前序版本的补丁版本（排除NA）
    versions = set()
    pre_versions = set()
    
    # 读取每一行的版本对应关系
    for line in data[1:]:
        current, pre = line.strip().split()
        versions.add(current)
        if pre != "NA":
            parent_map[current] = pre
            pre_versions.add(pre)
        else:
            parent_map[current] = None

    # 终结版为那些没有作为前序版本出现的补丁版本
    final_versions = [v for v in versions if v not in pre_versions]
    
    # 定义递归函数计算补丁升级的迭代次数
    memo = {}
    def chain_length(version):
        if version in memo:
            return memo[version]
        parent = parent_map.get(version)
        if parent is None:
            memo[version] = 1
        else:
            memo[version] = chain_length(parent) + 1
        return memo[version]
    
    max_length = 0
    ans = []
    for v in final_versions:
        length = chain_length(v)
        if length > max_length:
            max_length = length
            ans = [v]
        elif length == max_length:
            ans.append(v)
    ans.sort()  # 按字典序升序排序
    print(" ".join(ans))
    
if __name__ == "__main__":
    main()