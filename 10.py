# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time

allowed_domains = 'http://wooyun.org'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

def wooyun():
    for i in range(1,3600):
        page = str(i)
        url = str(allowed_domains)+'/bugs/page/' + str(page)
        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
            pattern = re.compile('<a href="(/bugs/wooyun.*?)">(.*?)</a>',re.S)
            items = re.findall(pattern,content)
            for item in items:
                print item[0],item[1]
        except urllib2.URLError, e:
             if hasattr(e,"code"):
                 print e.code
             if hasattr(e,"reason"):
                 print e.reason

if __name__=='__main__':
    wooyun()
