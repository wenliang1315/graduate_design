# -*- coding:utf-8 -*-
import os
import xlrd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")
import django

def weidu(fname):
    if django.VERSION >= (1, 7):  # 自动判断版本
        django.setup()

    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    sh = ''
    try:
        sh = bk.sheet_by_name("sheet1") #表单名称
    except:
        print ("no sheet in %s named Sheet1" % 'fname')
    #获取行数
    nrows = sh.nrows
    #获取列数
    ncols = sh.ncols
    print ("nrows %d, ncols %d" % (nrows,ncols))
    #获取第一行第一列数据
    #cell_value = sh.cell_value(1,1)
    row_list = []
    #获取各行数据
    for i in range(1,nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)

    jiaotongList = ['位置好','地铁','交通便利']
    huanjingList = ['宽敞', '干净', '整洁']
    fuwuList = ['房东回复','热情','周到']
    jiaotong = 0
    huanjing = 0
    fuwu = 0

    for i in range(nrows): #交通维度统计
        cell_value = sh.cell_value(i, 0)
        for j in range(0,len(jiaotongList)-1):
            if jiaotongList[j] in cell_value:
                jiaotong+= 1
                break

    for i in range(nrows): #环境维度统计
        cell_value = sh.cell_value(i, 0)
        for j in range(0,len(huanjingList)-1):
            if huanjingList[j] in cell_value:
                huanjing+= 1
                break

    for i in range(nrows): #服务维度统计
        cell_value = sh.cell_value(i, 0)
        for j in range(0,len(fuwuList)-1):
            if fuwuList[j] in cell_value:
                fuwu+= 1
                break

    print(jiaotongList,jiaotong)
    print(huanjingList,huanjing)
    print(fuwuList,fuwu)
    a = round((fuwu/nrows),2)*100
    b = round((huanjing/nrows),2)*100
    c = round((jiaotong/nrows),2)*100
    resultList=[]
    resultList.append(a)
    resultList.append(b)
    resultList.append(c)
    return resultList