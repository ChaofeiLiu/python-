import requests
from bs4 import BeautifulSoup

req = requests.get('https://developer.mozilla.org/zh-CN/')
print(req.status_code)
print(req.encoding)
print(req.cookies)

"""
print(type(req))
print(req.status_code)
print(req.encoding)
print(req.cookies)
"""