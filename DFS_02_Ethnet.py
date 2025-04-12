import sys

def main():
    # 读取所有输入数据
    data = sys.stdin.read().split()
    if not data:
        return
    # 第一行：读取矩阵的行数和列数
    n = int(data[0])
    m = int(data[1])
    
    # 构造网格矩阵
    grid = []
    index = 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[index]))
            index += 1
        grid.append(row)
    
    # 用于标记某个单元格是否已经访问过
    visited = [[False] * m for _ in range(n)]
    
    # DFS遍历，从 (i, j) 开始计算连通区域中 1 的数量
    def dfs(i, j):
        stack = [(i, j)]
        count = 0
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            count += 1
            # 遍历四个方向：上、下、左、右
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 1 and not visited[nx][ny]:
                        stack.append((nx, ny))
        return count
    
    max_count = 0
    # 遍历整个网格
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                size = dfs(i, j)
                if size > max_count:
                    max_count = size
    print(max_count)

if __name__ == "__main__":
    main()