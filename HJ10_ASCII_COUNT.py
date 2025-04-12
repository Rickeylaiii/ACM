import sys

def main():
    # 从标准输入读取一行数据，并去除首尾空白字符
    s = sys.stdin.readline().strip()
    
    # 利用 set() 统计字符串中不同字符的个数，
    # 只需判断这些字符是否在 ASCII 0 到 127 的范围内即可，
    # 题目保证了输入只包含 ASCII 33 到 126 的可见字符，所以 set(s) 即可。
    distinct_chars = set(s)
    
    # 输出集合中元素的个数
    print(len(distinct_chars))

if __name__ == "__main__":
    main()