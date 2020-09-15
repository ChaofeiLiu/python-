#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :Threadpool.py
# @Time :2020/9/15 
# @Author: chaofei_liu

from concurrent.futures import ThreadPoolExecutor

def sum(num):
    sum = 0
    for i in range(num+1):
        sum +=i
    return sum
pool = ThreadPoolExecutor(max_workers=20)

pool.submit()
