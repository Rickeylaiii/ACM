# -*- coding: gbk -*-
# 这段代码用于将输入的整数分解为质因数

# 从标准输入读取一个整数
n = int(input().strip())

# 存储所有质因数的列表
factors = []

# 先单独处理因子2
# 这样做可以在后续只需检查奇数因子，提高效率
while n % 2 == 0:
    factors.append(2)
    n //= 2  # n = n // 2，整除2

# 处理奇数质因子
# 从3开始，每次递增2（跳过所有偶数）
i = 3
while i * i <= n:  # 只需检查到sqrt(n)
    while n % i == 0:  # 如果i是n的因子
        factors.append(i)  # 添加到结果列表
        n //= i  # 将n除以i
    i += 2  # 检查下一个奇数

# 如果最后剩余的n大于1，则它必定是一个质数
# 因为所有小于sqrt(n)的质因子都已被提取
if n > 1:
    factors.append(n)

# 以空格分隔输出所有质因子
print(" ".join(map(str, factors)))