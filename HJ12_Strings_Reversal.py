import sys  # 导入sys模块，用于从标准输入读取数据

def main():
    # 从标准输入读取一行数据，并去掉首尾的空白字符
    n = sys.stdin.readline().strip()
    
    # 将输入字符串倒序排列
    rev = n[::-1]
    
    # 将结果列表中的字符拼接成字符串并输出
    print(rev)

# 如果当前模块是主程序，则执行main函数
if __name__ == "__main__":
    main()
