#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :ip_find.py
# @Time :2020/7/28 
# @Author: chaofei_liu

import requests
from bs4 import BeautifulSoup

input_ip = input('请输入您要查询的ip地址:')
url = 'https://www.ip138.com/iplookup.asp?ip={}&action=2'.format(input_ip)
proxy_browser = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url,headers=proxy_browser)
r.encoding =r.apparent_encoding
print(r.text[:1000])
