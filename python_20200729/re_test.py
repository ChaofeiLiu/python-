#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :re_test.py
# @Time :2020/7/29 
# @Author: chaofei_liu

import re
'''
finditer 每次返回可迭代对象，match对象
for m in re.finditer(r'[1-9]\d{5}','bit100081 xian100082 sichuan100083'):
    if m:
        print(m.group(0))
'''
'''
sub 替换函数 re.sub(匹配式，替换字符串，待匹配字符串)
text = re.sub(r'[1-9]\d{5}','zipcode','bit100081 xian100082 sichuan100083')
print(text)
'''
