#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :threading1.py
# @Time :2020/9/13 
# @Author: chaofei_liu

import threading
import time

def song():
    for i in range(3):
        print('song')
        time.sleep(1)

def dance():
    for i in range(3):
        print('dance')
        time.sleep(1)

if __name__ == '__main__':
    print('____开始____:%s' %time.ctime())
    t1 = threading.Thread(target=song())
    t2 = threading.Thread(target=dance())

    t1.start()
    t2.start()
    #time.sleep(5)
    print('____结束____%s' %time.ctime())


