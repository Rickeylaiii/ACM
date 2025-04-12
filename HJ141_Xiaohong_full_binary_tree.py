# -*- coding: gbk -*-
import sys

MOD = 10**9 + 7
n = int(input().strip())

if n == 1:
    print(0)
else:
    # 计算 2^(n-1) mod MOD （内置 pow() 支持模运算）
    p = pow(2, n - 1, MOD)
    # 根据公式计算答案，并取模
    result = (3 * p - 5) % MOD
    print(result)