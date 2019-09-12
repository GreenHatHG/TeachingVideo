# -*- coding: UTF-8 -*-
# 主程序

import study163
import utils
import bili
import merge
import sys
import openpyxl

file = "../resource/data.xlsx"

# 爬取的网站
websites = ('网易云课堂', 'Bilibili')

if __name__ == '__main__':
    # 检查resource文件夹下有没有xlsx文件，没有的话则创建
    utils.check(file)

    #接收命令行传递的参数，用于搜索关键字
    argv = sys.argv
    keyword = ""
    if len(argv) > 0 and argv is not None:
        keyword = argv[1]

    print('keyword =', keyword)

    for website in websites:
        utils.printStart(website)

        if website == '网易云课堂':
            study163.start(keyword, file)

        if website == 'Bilibili':
            bili.start(keyword, file)

        utils.printEnd(website)

    #对搜索到的结果进行过滤并且合并到一个sheet
    merge.merge(keyword, file)

    #使用openpyxl创建的表格默认带一个名字为"Sheet"的表格
    #该Sheet没有用处，所以去除
    wb = openpyxl.load_workbook(file)
    if 'Sheet' in str(wb.sheetnames):
        wb.remove(wb['Sheet'])
        wb.save(file)
        wb.close()