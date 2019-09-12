# -*- coding: UTF-8 -*-

import openpyxl


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
