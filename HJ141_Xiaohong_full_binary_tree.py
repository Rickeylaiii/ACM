# -*- coding: gbk -*-
import sys

MOD = 10**9 + 7
n = int(input().strip())

if n == 1:
    print(0)
else:
    # ���� 2^(n-1) mod MOD ������ pow() ֧��ģ���㣩
    p = pow(2, n - 1, MOD)
    # ���ݹ�ʽ����𰸣���ȡģ
    result = (3 * p - 5) % MOD
    print(result)