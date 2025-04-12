# -*- coding: gbk -*-
import sys

#���ݹ����
sys.setrecursionlimit(10000)

def count_regions_with_few_enemies():
    # ��ȡ����
    N, M, K = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    
    visited = [[False] * M for _ in range(N)]
    
    # �ĸ�������������
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    def dfs(x, y):
        # ͳ�Ƶ�ǰ�����е��˵�����
        enemy_count = 1 if grid[x][y] == 'E' else 0
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                # �������λ�ò���ǽ��û�з��ʹ�
                if grid[nx][ny] != '#' and not visited[nx][ny]:
                    enemy_count += dfs(nx, ny)
        return enemy_count

    region_count = 0
    # �������е�Ԫ��
    for i in range(N):
        for j in range(M):
            # ����ǿյػ������δ����
            if grid[i][j] != '#' and not visited[i][j]:
                count = dfs(i, j)
                if count < K:
                    region_count += 1
                    
    print(region_count)

if __name__ == '__main__':
    count_regions_with_few_enemies()
