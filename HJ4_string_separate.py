# -*- coding: gbk -*-
s = input().strip()

# ÿ8���ַ�һ��
for i in range(0, len(s), 8):
    part = s[i:i+8]
    # �������8���ַ�������0
    if len(part) < 8:
        part += '0' * (8 - len(part))
    print(part)