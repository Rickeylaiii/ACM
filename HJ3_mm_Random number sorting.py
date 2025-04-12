# -*- coding: gbk -*-
# 读取整数n，表示接下来要输入的随机数的数量
n = int(input().strip())

# 创建一个空集合，用于存储不重复的随机数
nums = set()

# 循环n次，读取n个随机数
for _ in range(n):
    # 读取一个整数并去除首尾空白字符
    num = int(input().strip())
    # 将整数添加到集合中，集合会自动去除重复的数字
    nums.add(num)

# 对集合中的数字进行排序，并逐个打印
# Python的sorted函数会返回一个已排序的列表
for num in sorted(nums):
    print(num)