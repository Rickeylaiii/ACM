# -*- coding: gbk -*-1 
from collections import deque
import sys

def generate_lucky_numbers(max_digits):
    # """
    # ʹ�ù���������� (BFS) �����������֡�
    
    # �������֣����������� '4' �� '7' ��������
    # ����:
    #     max_digits: �������ɵ��������ֵ����λ����������λ��ʱֹͣ���ɣ���
    # ����:
    #     ���������������ֵ������б�
    # """
    lucky = []  # ���ڱ������ɵ���������
    queue = deque(["4", "7"])  # BFS���У���ʼ������С����������

    while queue:
        s = queue.popleft()  # �Ӷ�����ȡ��һ����ǰ�����ַ���
        if len(s) > max_digits:
            continue  # �������λ�����������µ�����
        lucky.append(int(s))  # ����ǰ�ַ���ת��Ϊ������ӵ����������б���
        # �����µ��������֣�����ǰ���ֱַ���ĩβ׷�� "4" �� "7"
        queue.append(s + "4")
        queue.append(s + "7")
    
    return sorted(lucky)  # �������������������б�

def main():
    # ��ӡ��ʾ��Ϣ����֪�û��������䷶Χ
    print("�������������� l �� r���ÿո�������������� [l,r]����")
    # �ӱ�׼�����ȡ�������� l �� r
    l, r = map(int, input().split())
    
    # ���� r ��λ��ȷ�������������ֵ�λ�����ƣ�������һλ��ȷ���������п��ܷ�Χ
    max_digits = len(str(r)) + 1
    lucky_numbers = generate_lucky_numbers(max_digits)
    
    ans = 0  # �洢���ս�����ۼӺ�
    current = l  # ��ǰ��ʼ�����ۼӵ�λ�ã��� l ��ʼ

    # �����������ɵ��������֣�����С˳����
    for lucky in lucky_numbers:
        if lucky < current:
            continue  # �����������С�ڵ�ǰ��ʼֵ��������
        if current > r:
            break  # �����ǰֵ�Ѿ����� r������ѭ��
        # �����ڵ�ǰ lucky ���������£����� [current, lucky] �� [l, r] �Ľ������յ�
        segment_end = min(r, lucky)
        count = segment_end - current + 1  # ���㵱ǰ���ڵ���������
        ans += count * lucky  # ����ǰ�����������ֹ��׵�ֵ�ۼӵ� ans ��
        current = segment_end + 1  # ���µ�ǰ��ʼλ������һ������
        if current > r:
            break  # ������º����ʼֵ���� r������ѭ��

    # ������մ�
    print("��Ϊ:", ans)

if __name__ == '__main__':
    main()