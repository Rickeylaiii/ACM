# -*- coding: gbk -*-1 
from collections import deque
import sys

def generate_lucky_numbers(max_digits):
    # """
    # 使用广度优先搜索 (BFS) 生成幸运数字。
    
    # 幸运数字：仅包含数字 '4' 和 '7' 的整数。
    # 参数:
    #     max_digits: 限制生成的幸运数字的最大位数（超过该位数时停止生成）。
    # 返回:
    #     返回所有幸运数字的排序列表。
    # """
    lucky = []  # 用于保存生成的幸运数字
    queue = deque(["4", "7"])  # BFS队列，初始包含最小的幸运数字

    while queue:
        s = queue.popleft()  # 从队列中取出一个当前数字字符串
        if len(s) > max_digits:
            continue  # 超过最大位数则不再生成新的数字
        lucky.append(int(s))  # 将当前字符串转换为整数添加到幸运数字列表中
        # 生成新的幸运数字：将当前数字分别在末尾追加 "4" 和 "7"
        queue.append(s + "4")
        queue.append(s + "7")
    
    return sorted(lucky)  # 返回排序后的幸运数字列表

def main():
    # 打印提示信息，告知用户输入区间范围
    print("请输入两个整数 l 和 r（用空格隔开，代表区间 [l,r]）：")
    # 从标准输入读取两个整数 l 和 r
    l, r = map(int, input().split())
    
    # 根据 r 的位数确定生成幸运数字的位数限制，多生成一位以确保覆盖所有可能范围
    max_digits = len(str(r)) + 1
    lucky_numbers = generate_lucky_numbers(max_digits)
    
    ans = 0  # 存储最终结果的累加和
    current = l  # 当前开始积分累加的位置，从 l 开始

    # 遍历所有生成的幸运数字，按大小顺序处理
    for lucky in lucky_numbers:
        if lucky < current:
            continue  # 如果幸运数字小于当前起始值，则跳过
        if current > r:
            break  # 如果当前值已经大于 r，结束循环
        # 计算在当前 lucky 数字作用下，区间 [current, lucky] 与 [l, r] 的交集的终点
        segment_end = min(r, lucky)
        count = segment_end - current + 1  # 计算当前段内的数字数量
        ans += count * lucky  # 将当前段内所有数字贡献的值累加到 ans 中
        current = segment_end + 1  # 更新当前开始位置至下一个数字
        if current > r:
            break  # 如果更新后的起始值超出 r，结束循环

    # 输出最终答案
    print("答案为:", ans)

if __name__ == '__main__':
    main()