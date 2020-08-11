#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :JSON_demo.py
# @Time :2020/7/30 
# @Author: chaofei_liu
import json

'''
反序列化
json_str = '{"name":"LCF","age":22}'
student = json.loads(json_str)
print(type(student))
print(student['name'])
'''
# 序列化
student = {'name':'lcf','age':22,'flag':'False'}
json_str = json.dumps(student)
print(type(json_str))
print(json_str)