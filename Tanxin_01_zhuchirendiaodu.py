# -*- coding: gbk -*-1 
from typing import List
import heapq

class Solution:
    def minmumNumberOfHost(self, n: int, startEnd: List[List[int]]) -> int:
        # 按开始时间升序排序所有活动
        startEnd.sort(key=lambda x: x[0])
        
        # 使用最小堆存储各主持人的活动结束时间
        heap = []
        
        for event in startEnd:
            start, end = event[0], event[1]
            # 如果堆不为空，且最早结束的活动结束时间小于等于当前活动开始时间，
            # 则表示该主持人可以复用。（注意活动要求主持人全程参与，因此需确保时间上不冲突）
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            # 把当前活动的结束时间加入堆中，表示调配了一个主持人
            heapq.heappush(heap, end)
            
        # 最终堆中存储的元素个数即为同时进行活动最多的数量，也即最少需要的主持人数
        return len(heap)

if __name__ == '__main__':
    # 自定义输入格式：
    # 第一行输入活动数量 n
    # 后续 n 行，每行输入活动的开始时间和结束时间，以空格分隔
    n = int(input("请输入活动数量 n: "))
    events = []
    print("请输入每个活动的开始与结束时间（以空格分隔）：")
    for _ in range(n):
        s, e = map(int, input().split())
        events.append([s, e])
        
    solution = Solution()
    result = solution.minmumNumberOfHost(n, events)
    print("所需最少主持人数:", result)