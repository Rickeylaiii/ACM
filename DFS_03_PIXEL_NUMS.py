import sys
def count_pixel_boundaries():
    # Read input
    M, N = map(int, input().split())
    pixel_map = []
    for _ in range(M):
        row = list(map(int, input().split()))
        pixel_map.append(row)
    
    # Check if a position is within bounds
    def is_valid(x, y):
        return 0 <= x < M and 0 <= y < N
    
    # Identify boundary pixels (pixel 1 adjacent to a pixel 5)
    boundary_pixels = set()
    for i in range(M):
        for j in range(N):
            if pixel_map[i][j] == 1:
                # Check all 8 adjacent positions
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        adj_x, adj_y = i + dx, j + dy
                        if is_valid(adj_x, adj_y) and pixel_map[adj_x][adj_y] == 5:
                            boundary_pixels.add((i, j))
                            break
                    else:
                        continue
                    break
    
    # DFS to group adjacent boundary pixels
    def dfs(i, j, visited):
        visited.add((i, j))
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                adj_x, adj_y = i + dx, j + dy
                if (adj_x, adj_y) in boundary_pixels and (adj_x, adj_y) not in visited:
                    dfs(adj_x, adj_y, visited)
    
    # Count the number of distinct boundaries
    visited = set()
    boundary_count = 0
    for i, j in boundary_pixels:
        if (i, j) not in visited:
            boundary_count += 1
            dfs(i, j, visited)
    
    return boundary_count

print(count_pixel_boundaries())