#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :TongB_threading.py
# @Time :2020/9/13 
# @Author: chaofei_liu

import threading
import time

g_num = 0

def work1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁
    print('work1:{}'.format(g_num))

def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num +=1
        mutex.release()
    print('work2:{}'.format(g_num))


mutex = threading.Lock()         #  生成一个线程锁，防止引用全局变量混乱。

t1 = threading.Thread(target=work1,args=(1000000,))
t1.start()
t2 = threading.Thread(target=work2,args=(1000000,))
t2.start()

while len(threading.enumerate()) !=1:
    time.sleep(1)
print('ending_g_num:{}'.format(g_num))

