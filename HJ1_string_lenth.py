# -*- coding: gbk -*- 
# ����ϵͳģ�飬���ڶ�ȡ��׼����
import sys

def main():
    # ������׼�����ÿһ��
    for line in sys.stdin:
        # ȥ������β�Ŀհ��ַ�
        line = line.strip()
        # �����Ϊ�գ�������
        if not line:
            continue
        # ���ո�ָ��ַ����ɵ����б�
        words = line.split()
        # ��ȡ���һ������
        last_word = words[-1]
        # ������һ�����ʵĳ���
        print(len(last_word))

# ���ű���ֱ��ִ��ʱ����main����
if __name__ == '__main__':
    main()