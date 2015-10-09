#coding:utf-8
import urllib
import urllib2
import re,sys
import time

page = 1
url = 'http://www.wooyun.org/bugs/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile(r'/bugs/wooyun-\d-\d',re.S)
    for bugpath in p.findall(pattern):
       try:
           time.sleep(1)
           bugurl="http://www.wooyun.org/"+bugpath
           print str(bugurl)
