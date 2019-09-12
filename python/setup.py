# -*- coding: UTF-8 -*-

import study163
import utils
import bili
import merge
import sys
import openpyxl

file = "../resource/data.xlsx"
websites = ('网易云课堂', 'Bilibili')

if __name__ == '__main__':
    utils.check(file)

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

    merge.merge(keyword, file)

    wb = openpyxl.load_workbook(file)
    if 'Sheet' in str(wb.sheetnames):
        wb.remove(wb['Sheet'])
        wb.save(file)
        wb.close()