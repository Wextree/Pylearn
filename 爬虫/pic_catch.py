import requests

url = "http://pic13.nipic.com/20110409/7119492_114440620000_2.jpg"
path = "D://abc.jpg"

try:
    r = requests.get(url)
    with open(path,'wb') as f:
        f.write(r.content)
        print("文件保存成功！！")
except:
    print("爬取失败！！")