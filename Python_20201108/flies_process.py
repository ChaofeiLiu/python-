#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :flies_process.py
# @Time :2020/11/8 
# @Author: chaofei_liu
import sys
import time

def progress_bar():
    for i in range(1,101):
        print("\r",end="")
        print("Download progress: {}%:".format(i),"+" *(i//2),end="")
        sys.stdout.flush()
        time.sleep(0.05)

progress_bar()

