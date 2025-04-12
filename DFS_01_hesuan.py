import sys

def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    # 第一行：总人数 N
    n = int(input_lines[0].strip())
    # 第二行：确诊病例的人员编号（用逗号分隔），转换成整数集合
    confirmed = set(map(int, input_lines[1].strip().split(',')))
    
    # 从第三行开始读取接触矩阵，每行按逗号分隔
    matrix = []
    for i in range(2, 2+n):
        row = list(map(int, input_lines[i].strip().split(',')))
        matrix.append(row)
    
    # 用于记录通过感染传播链遍历到的人员编号
    reached = set()
    # 标记每个节点是否已经访问过
    visited = [False] * n

    def dfs(u):
        for v in range(n):
            # 当 u 和 v 有接触且 v 尚未访问时
            if matrix[u][v] == 1 and not visited[v]:
                visited[v] = True
                reached.add(v)
                dfs(v)
    
    # 对每个确诊病例进行 DFS 遍历
    # 注意：遍历时把确诊病例也标记为访问，以防止重复遍历
    for c in confirmed:
        if not visited[c]:
            visited[c] = True
            dfs(c)
    
    # 从传播链中去除确诊病例（它们本身不需要做检测）
    result = reached - confirmed
    print(len(result))

if __name__ == "__main__":
    main()