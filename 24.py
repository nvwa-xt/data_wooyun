# !/usr/bin python
#--*-- coding:utf-8 --*--
 
'''
批量下载任意网址上的图片
linux下的路径，有需要的改改路径，很简单，做为学习urllib模块的一个简单范例吧
'''
import os
import urllib
import re
 
url = ""
 
def getHtml(url):
    file = urllib.urlopen(url)
    html = file.read()
    return html
 
def getImageList(html):
    reg = 'http[^"]*?\.jpg'
    imgre = re.compile(reg)
    imgList = re.findall(imgre,html)
    return imgList
 
def printImageList(imgList):
    for i in imgList:
        print i
 
def download(imgList, page):
    x = 1
    for imgurl in imgList:
        print 'download file '+str(x)+' start'
        urllib.urlretrieve(imgurl,'./webImage/%s_%s.jpg'%(page,x))
        print 'download file '+ str(x)+ ' end'
        x+=1
 
 
def downImageNum(pagenum):
    page = 1
    pageNumber = pagenum
    while(page <= pageNumber):
        html = getHtml(url)#获得url指向的html内容
        imageList = getImageList(html)#获得所有图片的地址，返回列表
        printImageList(imageList)#打印所有的图片的地址
        download(imageList,page)#下载所有的图片
        page = page+1
 
if __name__ == '__main__':
    os.system('mkdir webImage')
    url = raw_input("enter the web page:")
    downImageNum(1)
