import requests

url = "http://www.baidu.com/s"
Keyword = 'Python'

try:
    kv = {'wd': Keyword}
    r = requests.get(url, params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败！！！")
