import requests
import re
url = 'https://bxqh66.com/html/category/photo/2019/0715/25164.html'
r = requests.get(url, timeout=30)
html = r.text
url_list = re.findall(r'https\:\/\/baxgood\.com\/p2\/20190710\-03\/\d{4}\.jpg',html)
print(url_list)