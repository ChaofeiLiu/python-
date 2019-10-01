import requests
import re
import os
def main():
    Url = 'https://bxqh66.com/html/category/photo/2019/0715/25164.html'
    root = "D:\demo\PICS\\"
    html = GetHtmlText(Url)
    pics_list = Pictrue_list(html)
    Download_pics(root,pics_list)

def GetHtmlText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "
def Pictrue_list(html):
    try:
        url_list = re.findall(r'https\:\/\/baxgood\.com\/p2\/20190710\-03\/\d{4}\.jpg',html)
        return url_list
    except:
        return " "
def Download_pics(root,url_list):
    for i in range(len(url_list)):
        path = root + url_list[i].split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url_list[i],timeout = 10)
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
                print("文件保存成功")
            else:
                print("文件已存在")
        except:
            print("爬取失败")


main()








