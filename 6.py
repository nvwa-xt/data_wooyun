#!/usr/bin/env python 
#-*-coding:utf-8-*-
'''
乌云漏洞网站 监控车市
''' 
###加载模块
import re
import urllib
from datetime import *
import time
import socket
import smtplib
import urllib2
 
##定义变量
url = "http://www.wooyun.org/searchbug.php?q=%E7%BD%91%E4%B8%8A%E8%BD%A6%E5%B8%82&showall=1"  ###自己网站的在乌云中搜索的url
 
###获取页面源代码
def source_html(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
 
def getitem(html):
	reg = r'提交日期：<.*>\d+-\d+-\d+</a>'
	imgre = re.compile(reg)
	srclist = re.findall(imgre,html)
	for list in srclist:
		return list
 
def getdate(list):
	reg = r'\d+-\d+-\d+'
	imgre = re.compile(reg)
	alldate = re.findall(imgre,list)
	for date in alldate:
		return date
 
def geturl(list):
	reg = r'href="(.*)"'
	imgre = re.compile(reg)
	alldate = re.findall(imgre,list)
	for date in alldate:
		return date
 
def send(message):
    url = "....." ## 自己公司的短信接口
    data = urllib.urlencode({'tel':'13800138000','con':message}) ###手机号
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    print response.read()
 
if __name__ == '__main__':
	html = source_html(url)
	list = getitem(html)
	if getdate(list) != date.today():
	 	message = "乌云网站有更新关于网上车市的漏洞。请及时查看 查看连接http://www.wooyun.org%s" %(geturl(list))
	 	print send(message)