import requests
import re
from bs4 import BeautifulSoup
r =requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
'''
tag = soup.a
name = soup.a.name
parent_name = soup.a.parent.name
attrs = soup.a.attrs
string = soup.p.string
print(soup.prettify())
print(name)
print(parent_name)
print(attrs)
print(string)
'''
a = soup.find_all('a')
print(a)
for tag in soup.find_all(True):
    print(tag.name,tag.attrs)
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

