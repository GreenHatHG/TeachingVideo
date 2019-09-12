import requests

def getText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '错误'


if __name__ == '__main__':
    url = "https://search.bilibili.com/all?keyword=spring&page=2"
    print(getText(url))
