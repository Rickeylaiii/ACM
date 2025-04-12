# -*- coding: gbk -*-
s = input().strip()

# 每8个字符一组
for i in range(0, len(s), 8):
    part = s[i:i+8]
    # 如果不足8个字符，补充0
    if len(part) < 8:
        part += '0' * (8 - len(part))
    print(part)