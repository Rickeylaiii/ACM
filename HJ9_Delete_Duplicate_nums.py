import sys  # 导入sys模块，用于从标准输入读取数据

def main():
    # 从标准输入读取一行数据，并去掉首尾的空白字符
    n = sys.stdin.readline().strip()
    
    # 将输入字符串倒序排列
    rev = n[::-1]
    
    # 创建一个集合，用于记录已经出现过的字符
    seen = set()
    
    # 创建一个列表，用于存储结果字符
    result = []
    
    # 遍历倒序后的字符串
    for ch in rev:
        # 如果当前字符尚未出现在集合中
        if ch not in seen:
            # 将字符添加到集合中，标记为已出现
            seen.add(ch)
            # 将字符添加到结果列表中
            result.append(ch)
    
    # 将结果列表中的字符拼接成字符串并输出
    print("".join(result))

# 如果当前模块是主程序，则执行main函数
if __name__ == "__main__":
    main()