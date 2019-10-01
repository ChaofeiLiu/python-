import requests
def Gettest(url):
    try:
        kv1 = {'user-agent':'Mozilla/5.0'} #代理访问信息需选择
        kv2 = {'wd':'python'}
        r = requests.get(url,timeout = 30,params= kv2)
        s = r.status_code
        r.raise_for_status()
        urlname= r.request.url
        return s,urlname,r.text[::1000],r.headers
    except:
        return "产生异常"
if __name__ == '__main__':
    url ="http://www.baidu.com/s"
    print(Gettest(url))