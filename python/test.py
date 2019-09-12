# -*- coding: UTF-8 -*-
# 用于检查需要爬取的信息能不能直接通过抓取网页源码得到

import requests

#得到网页源码
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
    url = "https://www.imooc.com/search/?words=java&page=1"
    print(getText(url))
