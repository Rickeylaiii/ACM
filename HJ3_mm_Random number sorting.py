# -*- coding: gbk -*-
# ��ȡ����n����ʾ������Ҫ����������������
n = int(input().strip())

# ����һ���ռ��ϣ����ڴ洢���ظ��������
nums = set()

# ѭ��n�Σ���ȡn�������
for _ in range(n):
    # ��ȡһ��������ȥ����β�հ��ַ�
    num = int(input().strip())
    # ��������ӵ������У����ϻ��Զ�ȥ���ظ�������
    nums.add(num)

# �Լ����е����ֽ������򣬲������ӡ
# Python��sorted�����᷵��һ����������б�
for num in sorted(nums):
    print(num)