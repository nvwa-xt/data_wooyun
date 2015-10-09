#!/usr/bin/python
#encoding:utf-8
import urllib
import os
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per
url = 'https://mm.taobao.com/687471686.htm'
#local = url.split('/')[-1]
local = os.path.join('/','687471686.htm')
urllib.urlretrieve(url,local,Schedule)
######output######
