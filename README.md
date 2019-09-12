<h1 align="center"><a href="https://github.com/GreenHatHG/TeachingVideo" target="_blank">关键字搜索网易云课堂与Bilibili</a></h1>
> Python3爬虫小Demo，自定义关键字搜索网易云课堂与Bilibili并保存到Excel

<p align="center">
<a href="#"><img alt="JDK" src="https://img.shields.io/badge/Python-3.7.4-yellow.svg?style=flat-square"/></a>
<img src="https://img.shields.io/badge/BeautifulSoup-4.8.0-green">
<img src="https://img.shields.io/badge/Openpyxl-2.6.3-yellowgreen">
<img src="https://img.shields.io/badge/license-Apache%202.0-blue">
</a>
</p>

------------------------------

# 效果

## 本次测试运行环境

![深度截图_选择区域_20190912224613.png](https://i.loli.net/2019/09/12/R2xlXT3hsK7HFMB.png)

## 运行过程

![运行效果](https://i.loli.net/2019/09/12/SDjIvzWpa4MRQlH.png)

![运行效果](https://i.loli.net/2019/09/12/sRD2SKr1Bv87G3l.png)

![运行效果](https://i.loli.net/2019/09/12/qrRlvG81Q3SaBoO.png)

## Excel

![深度截图_dde-desktop_20190912225342.png](https://i.loli.net/2019/09/12/Lv6gP8ZQcRuDEAz.png)
![深度截图_dde-desktop_20190912225437.png](https://i.loli.net/2019/09/12/Dz7lL8sfZ1ibYoE.png)
![深度截图_dde-desktop_20190912225446.png](https://i.loli.net/2019/09/12/icYHxaDVOPoM7tZ.png)
![深度截图_dde-desktop_20190912225413.png](https://i.loli.net/2019/09/12/I9ERPGXsrBVvNhn.png)
![深度截图_dde-desktop_20190912225350.png](https://i.loli.net/2019/09/12/qy2DHicMrhnEdSQ.png)
![深度截图_dde-desktop_20190912225420.png](https://i.loli.net/2019/09/12/vVHNfGS4Xl9Ecku.png)

# 运行方法

```sh
git clone https://github.com/GreenHatHG/TeachingVideo.git
cd TeachingVideo
python3 ./setup.py [关键字]
```

例子请看【效果】的第一张图

# 不足

1. 没有做到多平台支持，初衷是聚合各大学习视频网站，未加入网站：
   - [Lynda: Online Courses, Classes, Training, Tutorials](https://www.lynda.com/)
   - [极客学院IT在线教育平台-中国专业的IT职业在线教育平台](http://www.jikexueyuan.com/)
   - [慕课网-程序员的梦工厂](https://www.imooc.com/)
   - [在线做实验，高效学编程 - 实验楼](https://www.shiyanlou.com/)
   - [优达学城 (Udacity) 中国官网 - 传授硅谷的名企官方课程](https://cn.udacity.com/)

2. `Openpyxl`库性能不是那么好，存在数据量过大时无法写入`Excel`情况