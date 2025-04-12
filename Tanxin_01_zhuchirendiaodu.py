# -*- coding: gbk -*-1 
from typing import List
import heapq

class Solution:
    def minmumNumberOfHost(self, n: int, startEnd: List[List[int]]) -> int:
        # ����ʼʱ�������������л
        startEnd.sort(key=lambda x: x[0])
        
        # ʹ����С�Ѵ洢�������˵Ļ����ʱ��
        heap = []
        
        for event in startEnd:
            start, end = event[0], event[1]
            # ����Ѳ�Ϊ�գ�����������Ļ����ʱ��С�ڵ��ڵ�ǰ���ʼʱ�䣬
            # ���ʾ�������˿��Ը��á���ע��Ҫ��������ȫ�̲��룬�����ȷ��ʱ���ϲ���ͻ��
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            # �ѵ�ǰ��Ľ���ʱ�������У���ʾ������һ��������
            heapq.heappush(heap, end)
            
        # ���ն��д洢��Ԫ�ظ�����Ϊͬʱ���л����������Ҳ��������Ҫ����������
        return len(heap)

if __name__ == '__main__':
    # �Զ��������ʽ��
    # ��һ���������� n
    # ���� n �У�ÿ�������Ŀ�ʼʱ��ͽ���ʱ�䣬�Կո�ָ�
    n = int(input("���������� n: "))
    events = []
    print("������ÿ����Ŀ�ʼ�����ʱ�䣨�Կո�ָ�����")
    for _ in range(n):
        s, e = map(int, input().split())
        events.append([s, e])
        
    solution = Solution()
    result = solution.minmumNumberOfHost(n, events)
    print("����������������:", result)