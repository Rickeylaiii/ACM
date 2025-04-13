import sys
import heapq

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    # 第一行：站点总数（可用于校验，但本题中未做特殊使用）
    n = int(data[0].strip())
    
    # 第二行：出发站和到达站，空格分隔
    start, target = data[1].strip().split()
    
    # 构造图，邻接表形式，图为无向图
    graph = {}
    for line in data[2:]:
        if line.strip() == "0000":
            break
        # 例如输入格式：a b 5
        parts = line.strip().split()
        if len(parts) != 3:
            continue
        a, b, t = parts
        t = int(t)
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, t))
        graph[b].append((a, t))

    # Dijkstra 求最短路径
    dist = {station: float("inf") for station in graph}
    prev = {station: None for station in graph}
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        cur_d, u = heapq.heappop(heap)
        if cur_d > dist[u]:
            continue
        if u == target:
            break
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))
    
    # 重建路径
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    # 输出最短路径（各站点以空格分隔）
    print(" ".join(path))
    
if __name__ == "__main__":
    main()