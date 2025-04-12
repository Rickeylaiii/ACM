# -*- coding: gbk -*- 
# 导入系统模块，用于读取标准输入
import sys

def main():
    # 遍历标准输入的每一行
    for line in sys.stdin:
        # 去除行首尾的空白字符
        line = line.strip()
        # 如果行为空，则跳过
        if not line:
            continue
        # 按空格分割字符串成单词列表
        words = line.split()
        # 获取最后一个单词
        last_word = words[-1]
        # 输出最后一个单词的长度
        print(len(last_word))

# 当脚本被直接执行时调用main函数
if __name__ == '__main__':
    main()