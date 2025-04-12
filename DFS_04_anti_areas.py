# -*- coding: gbk -*-
import sys

#最大递归深度
sys.setrecursionlimit(10000)

def count_regions_with_few_enemies():
    # 读取输入
    N, M, K = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    
    visited = [[False] * M for _ in range(N)]
    
    # 四个方向：上下左右
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    def dfs(x, y):
        # 统计当前区域中敌人的数量
        enemy_count = 1 if grid[x][y] == 'E' else 0
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                # 如果相邻位置不是墙且没有访问过
                if grid[nx][ny] != '#' and not visited[nx][ny]:
                    enemy_count += dfs(nx, ny)
        return enemy_count

    region_count = 0
    # 遍历所有单元格
    for i in range(N):
        for j in range(M):
            # 如果是空地或敌人且未访问
            if grid[i][j] != '#' and not visited[i][j]:
                count = dfs(i, j)
                if count < K:
                    region_count += 1
                    
    print(region_count)

if __name__ == '__main__':
    count_regions_with_few_enemies()
