from cut import  cut_words_noun
from collections import Counter
import os
import xlrd
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")

def cutwords(fname):
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
    for i in range(0,nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)

    words = []
    for line in row_list:
        words.extend(cut_words_noun(line[0]))

    cutList = (Counter(words).most_common(15))

    return cutList

