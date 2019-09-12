# -*- coding: UTF-8 -*-

import openpyxl

# 检查resource文件夹下有没有xlsx文件，没有的话则创建
def check(file):
    try:
        openpyxl.load_workbook(file)
    except:
        wb = openpyxl.Workbook()
        wb.save(file)
        wb.close()

def printStart(text):
    print("--------------------------------")
    print("开始抓取：【" + text + "】")


def printEnd(text):
    print("停止抓取：【" + text + "】")
    print("--------------------------------")
