#calexp.py
from random import random
from time import perf_counter
zongdian=pow(10,5)
hit=0.0
start=perf_counter()
for i in range(1,zongdian+1):
             x,y=random(),random()
             r=pow(x**2+y**2,0.5)
             if r <=1.0:
                          hit=hit+1
pi=4*(hit/zongdian)
print("圆周率的值是：{}".format(pi))
print("系统的运行时间是：{:.5f}".format(perf_counter()-start))
