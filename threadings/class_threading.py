#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :class_threading.py
# @Time :2020/9/13 
# @Author: chaofei_liu

import threading
import time
class My_threading(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name + "  @  " +str(i)
            print(msg)

if __name__ == '__main__':
    t = My_threading()
    t.start()

