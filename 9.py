# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time
import pymongo
import random
import sys

f_handler=open('out.log', 'w') 
sys.stdout=f_handler

allowed_domains = 'http://wooyun.org'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
DOWNLOAD_DELAY = 1
connection = pymongo.Connection("localhost",27017)
db = connection.wooyun_list
collection = db.vulnerability_data

def wooyun():
    for i in range(1,3600):
        page = str(i)
        ##print u"------------------------------------------------------------"
        ##print u"this is page",page
        url = str(allowed_domains)+'/bugs/page/' + str(page)
        try:
            time.sleep(DOWNLOAD_DELAY)
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
            pattern = re.compile('<a href="(/bugs/wooyun.*?)">(.*?)</a>',re.S)
            items = re.findall(pattern,content)
            for item in items:
                print str(allowed_domains)+item[0],item[1]
                post = {"url":item[0],"title":item[1]}
                collection.insert(post)
                #print u"data is ok "
        except urllib2.URLError, e:
             if hasattr(e,"code"):
                 print e.code
             if hasattr(e,"reason"):
                 print e.reason

if __name__=='__main__':
    wooyun()
