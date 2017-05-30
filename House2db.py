
# -*- coding:utf-8 -*-
import os
import xlrd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")
import django

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()

def readExcel(fname):
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    sh = ''
    try:
        sh = bk.sheet_by_name("成都House") #表单名称
    except:
        print ("no sheet in %s named Sheet1" % fname)
    #获取行数
    nrows = sh.nrows
    #获取列数
    ncols = sh.ncols
    print ("nrows %d, ncols %d" % (nrows,ncols))
    #获取第一行第一列数据
    cell_value = sh.cell_value(1,1)
    row_list = []
    #获取各行数据
    for i in range(1,nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)
    return row_list

def main():
    from djangoweliang.models import House

    f = '成都House.xlsx'
    content = readExcel(f)
    WorkList = []

    for parts in content:
        WorkList.append(House(name=parts[0], city=parts[1], price=parts[2], area=parts[3], numofman=parts[4],bedsize=parts[5]
            )
        )
    House.objects.bulk_create(WorkList)

if __name__ == "__main__":
    main()
    print('Done!')