#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :python_files.py
# @Time :2020/7/31 
# @Author: chaofei_liu
import os

f = open('D:\\pycharm2020.1\\chaofei_liu\\python_20200731\\demo_txt.txt','a+')
'''
tf = f.readlines()
for line in tf:
    print(line)
f.close()
'''
ls = ['*','china','england','japan','*','   ']
f.writelines(ls)   # f.readlines(),f.writelines(),均返回列表，（可循环遍历）
f.seek(0)  # 文件指针  seek(0) 文件开头  seek(1) 文件当前位置   seek(2)  文件结尾
for line in f:
    print(line)
f.close()