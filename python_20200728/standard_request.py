#!/usr/bin/env/ python
# -*— coding=utf-8 -*-
# @FileName :standard_request.py.py
# @Time :2020/7/28 
# @Author: chaofei_liu

import requests

def get_HTML(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__ == "__main__":
    url = 'https://www4.bing.com/?scope=web&wlexpsignin=1'

    """
    模拟浏览器访问
    kv = {'user-agent': 'Mozilla/5.0'}
    r =requests.get(url,headers=kv)
    print(r.status_code)
    """

    print(get_HTML(url))