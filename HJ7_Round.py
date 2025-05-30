
"""
此程序实现浮点数的四舍五入功能。

功能描述:
    读取用户输入的浮点数，将其四舍五入为最接近的整数并输出结果。

实现方法:
    通过 int(x + 0.5) 公式进行四舍五入操作。
    - 当小数部分 < 0.5 时，向下取整
    - 当小数部分 >= 0.5 时，向上取整

输入:
    一个浮点数

输出:
    四舍五入后的整数

示例:
    输入: 5.5
    输出: 6
    
    输入: 2.3
    输出: 2
"""
x = float(input().strip())
result = int(x + 0.5)
print(result)