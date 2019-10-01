import requests
def GetHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers = kv,timeout = 30)
        s= r.status_code
        requests.head(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return s,r.text[1000:2000],r.headers
    except:
        return "产生异常"
if __name__ == "__main__":
    url = "https://bxqh22.com/html/category/photo/2019/0715/25163.html"
    print(GetHTMLText(url))