# --- coding: gbk -*-
import sys

def get_total_size():
    # 读取 M（目录个数）和查询目录 id
    M, query_id = input().split()
    M = int(M)
    query_id = int(query_id)
    
    # 构造目录信息字典：{目录id: (大小, [子目录id列表])}
    dirs = {}
    for _ in range(M):
        line = input().strip()
        # 格式示例: "1 20 (2,3)" 或 "3 15 ()"
        parts = line.split()
        dir_id = int(parts[0])
        size = int(parts[1])
        # 去掉括号，即去掉第一个"("和最后一个字符")"
        # parts[2] = "(2,3)" 或 "()"
        children_str = parts[2][1:-1]
        if children_str:
            children = list(map(int, children_str.split(',')))
        else:
            children = []
        dirs[dir_id] = (size, children)
    
    # DFS 递归计算目录总大小
    def dfs(cur_id):
        cur_size, children = dirs[cur_id]
        total = cur_size
        for child in children:
            total += dfs(child)
        return total
    
    print(dfs(query_id))

if __name__ == '__main__':
    get_total_size()