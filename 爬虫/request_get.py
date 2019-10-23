import requests

# 现行框架：封装好的一个函数
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，就抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Eorro"

if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(getHtmlText(url))
