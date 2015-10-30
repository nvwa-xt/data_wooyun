# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

#等待认领的漏洞
url = 'http://apis.baidu.com/apistore/wooyun/unclaim?limit=10'

#最新公开的漏洞
#url = 'http://apis.baidu.com/apistore/wooyun/public?limit=10'

#最新确认的漏洞
#url = 'http://apis.baidu.com/apistore/wooyun/confirm?limit=10'

#最新提交的漏洞
#url = 'http://apis.baidu.com/apistore/wooyun/submit?limit=10'

req = urllib2.Request(url)

req.add_header("apikey", "b09c696d7853aaf0f15638a5bc2e3c12")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
