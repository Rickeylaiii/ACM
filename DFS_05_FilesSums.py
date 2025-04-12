# --- coding: gbk -*-
import sys

def get_total_size():
    # ��ȡ M��Ŀ¼�������Ͳ�ѯĿ¼ id
    M, query_id = input().split()
    M = int(M)
    query_id = int(query_id)
    
    # ����Ŀ¼��Ϣ�ֵ䣺{Ŀ¼id: (��С, [��Ŀ¼id�б�])}
    dirs = {}
    for _ in range(M):
        line = input().strip()
        # ��ʽʾ��: "1 20 (2,3)" �� "3 15 ()"
        parts = line.split()
        dir_id = int(parts[0])
        size = int(parts[1])
        # ȥ�����ţ���ȥ����һ��"("�����һ���ַ�")"
        # parts[2] = "(2,3)" �� "()"
        children_str = parts[2][1:-1]
        if children_str:
            children = list(map(int, children_str.split(',')))
        else:
            children = []
        dirs[dir_id] = (size, children)
    
    # DFS �ݹ����Ŀ¼�ܴ�С
    def dfs(cur_id):
        cur_size, children = dirs[cur_id]
        total = cur_size
        for child in children:
            total += dfs(child)
        return total
    
    print(dfs(query_id))

if __name__ == '__main__':
    get_total_size()